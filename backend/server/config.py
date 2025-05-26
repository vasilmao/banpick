import os
from dotenv import load_dotenv
import logging

load_dotenv()

class Config:
    version = "0.1.0"
    title = "sales_scope"
    
    app_settings = {
        'tour_db_name': os.getenv('MONGO_DB_TOUR'),
        'tour_collection': os.getenv('MONGO_COLLECTION_TOUR'),
        'mongodb_url': os.getenv('MONGO_URL'),
        'mongodb_port': os.getenv('MONGO_PORT'),
        'login': os.getenv('MONGODB_LOGIN'),
        'password': os.getenv('MONGODB_PASSWORD'),
    }

    @classmethod
    def app_settings_validate(cls):
        for k, v in cls.app_settings.items():
            if None is v:
                logging.error(f'Config variable error. {k} cannot be None')
                raise Exception([{"message": "Server configure error"}])
            else:
                logging.info(f'Config variable {k} is {v}')
