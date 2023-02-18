import json
from kafka import KafkaConsumer, TopicPartition

host = 'rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091'
topic = 'zsmk-9433-dev-01'
user = '9433_reader'
password = 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK'

SASL_MECHANISM = "SCRAM-SHA-512"
SASL_SSL = "SASL_SSL"

consumer = KafkaConsumer(bootstrap_servers=host, group_id="sdelaisam1", ssl_cafile="ca.pem",
                         sasl_mechanism=SASL_MECHANISM, sasl_plain_username=user, sasl_plain_password=password,
                         security_protocol="SASL_SSL", enable_auto_commit=True, auto_commit_interval_ms=30 * 1000,
                         auto_offset_reset='earliest')
my_partition = TopicPartition(topic, 0)
consumer.assign([my_partition])
consumer.seek_to_beginning(my_partition)
for message in consumer:
    parsed_data = json.loads(message.value.decode())
    print(len(parsed_data.keys()))
# consumer.close()
