import json


class Settings:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_settings(self, settings):
        with open(self.filename, 'w') as file:
            json.dump(settings, file, indent=4)
