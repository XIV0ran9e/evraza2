import json
import asyncio
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

consumer = AIOKafkaConsumer(bootstrap_servers=host, group_id="sdelaisam1",
                            ssl_context=create_ssl_context(cafile="ca.pem"),
                            sasl_mechanism=SASL_MECHANISM, sasl_plain_username=user, sasl_plain_password=password,
                            security_protocol="SASL_SSL", enable_auto_commit=True, auto_commit_interval_ms=30 * 1000,
                            auto_offset_reset='earliest')

with open('mapping.json', encoding='utf-8') as f:
    mapping: dict = json.loads(f.read())

important_signals = mapping.keys()


async def messages_listener(consumer: AIOKafkaConsumer):
    my_partition = TopicPartition(topic, 0)
    consumer.assign([my_partition])
    # await consumer.seek_to_beginning(my_partition)
    await consumer.start()
    consumer.seek(my_partition, 0)
    async for message in consumer:
        parsed_data = json.loads(message.value.decode())
        current_dt = datetime.fromisoformat(parsed_data['moment'])
        msg = {
            'dt': parsed_data['moment'],
            'warnings': [],
            'data': {}
        }

        for s in important_signals:
            current_val = parsed_data.get(s)
            signal_map = mapping.get(s)
            if signal_map['has_warnings']:
                if current_val is None:
                    msg['warnings'].append(
                        {'type': 'missing', "signal": s}
                    )
                    continue
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
                msg['data'][s] = {
                    'name': mapping[s]['name'],
                    'value': current_val,
                    'has_warning': True,
                    'alarm_min': parsed_data[signal_map['alarm_min']],
                    'alarm_max': parsed_data[signal_map['alarm_max']],
                    'warning_min': parsed_data[signal_map['warning_min']],
                    'warning_max': parsed_data[signal_map['warning_max']]
                }
            else:
                msg['data'][s] = {
                    'name': mapping[s]['name'],
                    'value': current_val,
                    'has_warning': False
                }
        yield msg
        await asyncio.sleep(1)
