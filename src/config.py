import yaml


class Configuration:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None

    def _load_config(self):
        with open(self.config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_value(self, key):
        if self.config is None:
            self._load_config()
        return self.config.get(key)
