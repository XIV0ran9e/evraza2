from typing import Optional
from datetime import datetime, timedelta
from pymongo import MongoClient
from . import settings


class MongoManager:
    __instance: Optional[MongoClient] = None
    DB = 'evraza2'
    collection_by_day = 'records_{}_{}_{}'

    client: MongoClient = None

    def connect(self):
        self.client: MongoClient = MongoClient(
            settings.MONGO_HOST, settings.MONGO_PORT,
            username=settings.MONGO_USERNAME,
            password=settings.MONGO_PASSWORD
        )

    def disconnect(self):
        self.client.close()

    def write_new_msg(self, document, dt: datetime):
        col = self.client[self.DB][self.collection_by_day.format(dt.day, dt.month, dt.year)]
        col.insert_one(document)

    def get_last_one(self):
        db = self.client[self.DB]
        start_dt = datetime(day=25, month=1, year=2023)
        temp_dt = start_dt + timedelta(days=1)
        while db[self.collection_by_day.format(temp_dt.day, temp_dt.month, temp_dt.year)].count_documents({}) > 0:
            start_dt = temp_dt
            temp_dt += timedelta(days=1)
        col = db[self.collection_by_day.format(start_dt.day, start_dt.month, start_dt.year)]
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
        r = aggregation.next()
        r.pop('_id')
        r['moment_dt'] = r['moment_dt'].isoformat()
        return r
