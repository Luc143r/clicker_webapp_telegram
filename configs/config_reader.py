import os
import json
import codecs


class Config:
    def __init__(self, type_config: int, data: dict):
        if type_config == 0:
            # config.json
            self.TOKEN = data['TOKEN']
            self.API_URL = data['API_URL']
            self.DB_HOST = data['DB_HOST']
            self.DB_PORT = data['DB_PORT']
            self.DB_USER = data['DB_USER']
            self.DB_PASSWORD = data['DB_PASSWORD']
        elif type_config == 1:
            # boost_config.json
            self.NAME = data['NAME']
            self.START_PRICE = data['START_PRICE']
            self.PRICE_STEP = data['PRICE_STEP']
            self.MAX_LVL = data['MAX_LVL']


    @staticmethod
    def get_config(type_config: int, config_file: str) -> dict:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(f'{this_dir}/../configs/{config_file}.json')
        with codecs.open(full_path, 'r', encoding='utf-8') as config:
            data = json.load(config)
        return Config(type_config, data)
