import deepl
import logging

logging.getLogger('deepl').setLevel(logging.DEBUG)

class DeeplTranslate(object):
    def __init__(self, auth_key: str, source_lang: str, target_lang: str):
        self.translator = deepl.Translator(auth_key)
        self.source_lang = source_lang
        self.target_lang = target_lang

    def translate(self, text: str) -> str:
        return self.translator.translate_text(text, source_lang=self.source_lang, target_lang=self.target_lang).text
