from typing import Optional
from pymongo import MongoClient
from backend import settings


class MongoManager:
    __instance: Optional[MongoClient] = None
    DB = 'evraza2'

    client: MongoClient = None

    def connect(self):
        self.client: MongoClient = MongoClient(
            settings.MONGO_HOST, settings.MONGO_PORT,
            username=settings.MONGO_USERNAME,
            password=settings.MONGO_PASSWORD
        )

    def disconnect(self):
        self.client.close()
