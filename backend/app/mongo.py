from typing import Optional
from datetime import datetime, timedelta
from pymongo import MongoClient
from . import settings


class MongoManager:
    __instance: Optional[MongoClient] = None
    DB = 'evraza2'
    collection_by_day = 'records_{}_{}_{}'
    metadatacol = 'metadatacol'

    client: MongoClient = None

    def connect(self):
        self.client: MongoClient = MongoClient(
            settings.MONGO_HOST, settings.MONGO_PORT,
            username=settings.MONGO_USERNAME,
            password=settings.MONGO_PASSWORD
        )

    def disconnect(self):
        self.client.close()

    def get_last_offset(self):
        col = self.client[self.DB][self.metadatacol]
        d = col.find_one({})
        if d:
            return d['offset']
        else:
            return 0

    def write_last_offset(self, offset):
        col = self.client[self.DB][self.metadatacol]
        d = col.find_one({})
        if d is None:
            col.insert_one({'offset': offset})
        else:
            col.update_one({'_id': d['_id']}, {'$set': {'offset': offset}})

    def write_new_msg(self, document, dt: datetime):
        col = self.client[self.DB][self.collection_by_day.format(dt.day, dt.month, dt.year)]
        document['moment_dt'] = dt
        if col.find_one({'moment': dt.isoformat()}):
            col.update_one({'moment': dt.isoformat()},
                           {'$set': document}
                           )
        else:
            col.insert_one(document)

    def get_last_one(self):
        db = self.client[self.DB]
        # start_dt = datetime(day=25, month=1, year=2023)
        # temp_dt = start_dt + timedelta(days=1)
        # while db[self.collection_by_day.format(temp_dt.day, temp_dt.month, temp_dt.year)].count_documents({}) > 0:
        #     start_dt = temp_dt
        #     temp_dt += timedelta(days=1)
        col = db["records_19_2_2023"]
        aggregation = col.aggregate(
            [
                {
                    "$addFields": {
                        "moment_dt": {
                            "$dateFromString": {
                                "dateString": "$moment"
                            }
                        }
                    }
                },
                {
                    "$sort": {
                        "moment_dt": -1
                    }
                }
            ]
        )
        try:
            r = aggregation.next()
            r.pop('_id')
            r['moment_dt'] = r['moment_dt'].isoformat()
            return r
        except StopIteration:
            return {}

    def get_graphics(self, fields, date_from: datetime, date_to: datetime):
        datasets = []
        labels = []
        # date_from.day
        while date_from < date_to:
            col = self.client[self.DB][self.collection_by_day.format(date_from.day, date_from.month, date_from.year)]
            col.aggregate(
                [
                    {
                        '$addFields': {
                            'moment_dt': {
                                '$dateFromString': {
                                    'dateString': '$moment'
                                }
                            }
                        }
                    }, {
                    '$addFields': {
                        'y': {
                            '$year': '$moment_dt'
                        },
                        'm': {
                            '$month': '$moment_dt'
                        },
                        'd': {
                            '$dayOfMonth': '$moment_dt'
                        },
                        'h': {
                            '$hour': '$moment_dt'
                        }
                    }
                }, {
                    '$sort': {
                        'moment_dt': 1
                    }
                }, {
                    '$group': {
                        '_id': {
                            'year': '$y',
                            'month': '$m',
                            'day': '$d',
                            'hour': '$h'
                        },
                        'total': {
                            '$avg': '$SM_Exgauster\\[0:4]'
                        },
                        'total2': {
                            '$avg': '$SM_Exgauster\\[1:4]'
                        }
                    }
                }
                ]
            )
            date_from += timedelta(minutes=1)
