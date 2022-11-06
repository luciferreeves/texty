import json
import os


class PreferenceManager:
    def __init__(self, default_prefs, preferences_file):
        self.DEFAULT_PREFS, self.preferences = default_prefs, default_prefs
        self.preferences_file = preferences_file
        self.load()

    def load(self):
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, "r") as f:
                self.preferences = json.load(f)

    def save(self):
        with open(self.preferences_file, "w") as f:
            json.dump(self.preferences, f)

    def get(self, key):
        return self.preferences[key]

    def set(self, key, value):
        self.preferences[key] = value

    def reset(self):
        self.preferences = self.DEFAULT_PREFS
        self.save()
