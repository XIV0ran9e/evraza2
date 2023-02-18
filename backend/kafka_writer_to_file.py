import json
from datetime import datetime
from kafka import KafkaConsumer, TopicPartition
from backend.app.mongo import MongoManager

host = 'rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091'
topic = 'zsmk-9433-dev-01'
user = '9433_reader'
password = 'eUIpgWu0PWTJaTrjhjQD3.hoyhntiK'

SASL_MECHANISM = "SCRAM-SHA-512"
SASL_SSL = "SASL_SSL"
consumer = KafkaConsumer(bootstrap_servers=host, group_id="sdelaiisam1", ssl_cafile="ca.pem",
                         sasl_mechanism=SASL_MECHANISM, sasl_plain_username=user, sasl_plain_password=password,
                         security_protocol="SASL_SSL", enable_auto_commit=True, auto_commit_interval_ms=30 * 1000,
                         auto_offset_reset='earliest')

if __name__ == '__main__':
    mm = MongoManager()
    mm.connect()
    my_partition = TopicPartition(topic, 0)
    consumer.assign([my_partition])
    consumer.seek_to_beginning(my_partition)
    for message in consumer:
        parsed_data = json.loads(message.value.decode())
        dt = datetime.fromisoformat(parsed_data['moment'])
        mm.write_new_msg(parsed_data, dt)
