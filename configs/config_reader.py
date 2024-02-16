import os
import json
import codecs


class Config:
    def __init__(self, data):
        # config.json
        self.TOKEN = data['TOKEN']
        self.API_URL = data['API_URL']
        self.DB_HOST = data['DB_HOST']
        self.DB_PORT = data['DB_PORT']
        self.DB_USER = data['DB_USER']
        self.DB_PASSWORD = data['DB_PASSWORD']

        # boost_config.json


    @staticmethod
    def get_config(config_file):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(f'{this_dir}/../configs/{config_file}.json')
        with codecs.open(full_path, 'r', encoding='utf-8') as config:
            data = json.load(config)
        return Config(data)
