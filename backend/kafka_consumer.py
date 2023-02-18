import json
from kafka import KafkaConsumer, TopicPartition

# host = 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091'
host = 'rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091'
topic = 'zsmk-9433-dev-01'
user = '9433_reader'
password = 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK'

SASL_MECHANISM = "SCRAM-SHA-512"
SASL_SSL = "SASL_SSL"

consumer = KafkaConsumer(bootstrap_servers=host, group_id="sdelaisam1", ssl_cafile="backend/ca.pem",
                         sasl_mechanism=SASL_MECHANISM, sasl_plain_username=user, sasl_plain_password=password,
                         security_protocol="SASL_SSL", enable_auto_commit=True, auto_commit_interval_ms=30 * 1000,
                         auto_offset_reset='earliest')
my_partition = TopicPartition(topic, 0)
consumer.assign([my_partition])
consumer.seek_to_beginning(my_partition)

with open('backend/mapping.json', encoding='utf-8') as f:
    mapping: dict = json.loads(f.read())

important_signals = mapping.keys()

for message in consumer:
    parsed_data = json.loads(message.value.decode())
    print(parsed_data['moment'])
    for s in important_signals:
        current_val = parsed_data.get(s)
        signal_map = mapping.get(s)
        if signal_map['has_warnings']:
            if current_val > parsed_data[signal_map['warning_max']]:
                print('warning max !', round(current_val, 6), mapping[s]['name'])
            elif current_val > parsed_data[signal_map['alarm_max']]:
                print('alarm max !', round(current_val, 6), mapping[s]['name'])

            if current_val < parsed_data[signal_map['warning_min']]:
                print('warning min !', round(current_val, 6), mapping[s]['name'])
            elif current_val < parsed_data[signal_map['alarm_min']]:
                print('alarm min !', round(current_val, 6), mapping[s]['name'])
