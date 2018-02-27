import os
import yaml

CONFIG_FILE = os.environ.get('CONFIG_FILE', '')
SENSU_API_URI = os.environ.get('SENSU_API_URI', 'http://localhost:4567/results')
DEBUG = bool(os.environ.get('DEBUG', 'False').lower() in ("true", "yes", "t", "1"))


def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as e:
            raise e
    return config


def validate_api_key(apikey, config, data):
    apikey = str(apikey).lower()
    try:
        return (config[apikey]['source'] == data['source'])
    except KeyError as e:
        return False
    return False
