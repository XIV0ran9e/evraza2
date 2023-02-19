import json
import asyncio
from collections import defaultdict
from datetime import datetime
from aiokafka import AIOKafkaConsumer, TopicPartition
from aiokafka.helpers import create_ssl_context

# host = 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091' # old host
host = 'rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091'
topic = 'zsmk-9433-dev-01'
user = '9433_reader'
password = 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK'

SASL_MECHANISM = "SCRAM-SHA-512"
SASL_SSL = "SASL_SSL"


class MagicNumbers:
    VIBRATION_HORIZONTAL_SEVEN = 1.71990613e-05
    VIBRATION_VERTICAL_SEVEN = 2.60824919e-05
    VIBRATION_AXIAL_SEVEN = 9.08204869e-06
    VIBRATION_AXIAL_EIGHT = 4.2977256e-05


DAY_IN_DOTS = 60 * 24

exhausters = {
    "Эксгаустер № 1 (У-171)": 1,
    "Эксгаустер № 2 (У-172)": 2,
    "Эксгаустер № 3 (Ф-171)": 3,
    "Эксгаустер № 4 (Ф-172)": 4,
    "Эксгаустер № 5 (X-171)": 5,
    "Эксгаустер № 6 (X-172)": 6,
}

aglomachines = {
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 1,
    6: 1
}

consumer = AIOKafkaConsumer(bootstrap_servers=host, group_id="sdelaisam1",
                            ssl_context=create_ssl_context(cafile="ca.pem"),
                            sasl_mechanism=SASL_MECHANISM, sasl_plain_username=user, sasl_plain_password=password,
                            security_protocol="SASL_SSL", enable_auto_commit=True, auto_commit_interval_ms=30 * 1000,
                            auto_offset_reset='earliest')

with open('mapping.json', encoding='utf-8') as f:
    mapping: dict = json.loads(f.read())

important_signals = mapping.keys()


def parse_message(parsed_data: dict):
    current_dt = datetime.fromisoformat(parsed_data['moment'])
    msg = {
        'dt': parsed_data['moment'],
        'warnings': [],
        'aglomachines': {
            "1": [],
            "2": [],
            "3": []
        }
    }
    exhausters_data = {}
    for i in range(1, 7):
        exhausters_data[i] = {}

    forecasts = defaultdict(list)
    for s in important_signals:
        current_val = parsed_data.get(s)
        signal_map = mapping.get(s)
        exhauster_id = exhausters[signal_map['number']]

        def breakdown_forecast():
            def check_signal(part, enum, magic_number):
                if parsed_data[signal_map['current_part']] == part and parsed_data[signal_map['enum']] == enum:
                    border = parsed_data[signal_map['warning_max']]  # todo а правда, что эту?
                    return (border - current_val) / magic_number

            forecast = [
                check_signal('Подшипник 7', 'vibration_horizontal', MagicNumbers.VIBRATION_HORIZONTAL_SEVEN),
                check_signal('Подшипник 7', 'vibration_vertical', MagicNumbers.VIBRATION_VERTICAL_SEVEN),
                check_signal('Подшипник 7', 'vibration_axial', MagicNumbers.VIBRATION_AXIAL_SEVEN),
                check_signal('Подшипник 8', 'vibration_axial', MagicNumbers.VIBRATION_AXIAL_EIGHT),
            ]
            forecasts[exhauster_id].extend(filter(lambda x: x is not None, forecast))

        if signal_map['has_warnings']:
            if current_val is None:
                msg['warnings'].append(
                    {'type': 'missing', "signal": s}
                )
                continue

            breakdown_forecast()

            if current_val > parsed_data[signal_map['warning_max']]:
                msg['warnings'].append(
                    {'type': 'warning max !', 'value': round(current_val, 6), 'name': mapping[s]['name'],
                     "signal": s}
                )
            elif current_val > parsed_data[signal_map['alarm_max']]:
                msg['warnings'].append(
                    {'type': 'alarm max !', 'value': round(current_val, 6), 'name': mapping[s]['name'], "signal": s}
                )
            if current_val < parsed_data[signal_map['warning_min']]:
                msg['warnings'].append(
                    {'type': 'warning min !', 'value': round(current_val, 6), 'name': mapping[s]['name'],
                     "signal": s}
                )
            elif current_val < parsed_data[signal_map['alarm_min']]:
                msg['warnings'].append(
                    {'type': 'alarm min !', 'value': round(current_val, 6), 'name': mapping[s]['name'], "signal": s}
                )
            exhausters_data[exhauster_id][s] = {
                'name': mapping[s]['name'],
                'value': current_val,
                'has_warning': True,
                'alarm_min': parsed_data[signal_map['alarm_min']],
                'alarm_max': parsed_data[signal_map['alarm_max']],
                'warning_min': parsed_data[signal_map['warning_min']],
                'warning_max': parsed_data[signal_map['warning_max']],
                'number': mapping[s]['number'],
            }
        else:
            exhausters_data[exhauster_id][s] = {
                'name': mapping[s]['name'],
                'value': current_val,
                'has_warning': False,
                'number': mapping[s]['number']
            }
    for i in range(1, 7):
        exhausters_data[i]['breakdown_forecast'] = min(forecasts[i])
    msg['aglomachines']['1'].append(exhausters_data[1])
    msg['aglomachines']['1'].append(exhausters_data[2])
    msg['aglomachines']['2'].append(exhausters_data[3])
    msg['aglomachines']['2'].append(exhausters_data[4])
    msg['aglomachines']['3'].append(exhausters_data[5])
    msg['aglomachines']['3'].append(exhausters_data[6])
    return msg


async def messages_listener(consumer: AIOKafkaConsumer):
    my_partition = TopicPartition(topic, 0)
    consumer.assign([my_partition])
    await consumer.start()
    # consumer.seek(my_partition, 0)
    await consumer.seek_to_end(my_partition)
    print()
    async for message in consumer:
        yield parse_message(json.loads(message.value.decode()))
