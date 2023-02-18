from typing import Optional
from datetime import datetime
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
