import json
import os

class Translator:
    def __init__(self, lang="en"):
        self.lang = lang
        self.translations = {}
        self.load_language(lang)

    def load_language(self, lang):
        path = os.path.join(os.path.dirname(__file__)+"/translations", f"{lang}.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
        except FileNotFoundError:
            self.translations = {}

    def set_language(self, lang):
        self.lang = lang
        self.load_language(lang)

    def tr(self, key):
        return self.translations.get(key, key)