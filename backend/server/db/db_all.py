from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
# from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
import logging

from server.config import Config

load_dotenv()

db_tournament: Database = None

def connect_and_init_db():
    global db_tournament
    print(Config.app_settings.get('mongodb_url'))
    print(Config.app_settings.get('login'))
    print(Config.app_settings.get('password'))
    try:
        db_client = MongoClient(
            Config.app_settings.get('mongodb_url'),
            int(Config.app_settings.get('mongodb_port')),
            username=Config.app_settings.get('login'),
            password=Config.app_settings.get('password'),
            uuidRepresentation="standard",
        )
        logging.info('Connected to mongo.')
        db_tournament = db_client[Config.app_settings.get('tour_db_name')]
    except Exception as e:
        print('Not connected to mongo')
        logging.exception(f'Could not connect to mongo: {e}')
        raise

def get_tournament_collection() -> Collection:
    tournament_collection = db_tournament[Config.app_settings.get('tour_collection')]
    return tournament_collection
