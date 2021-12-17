"""Sends the stt text to DeepL to be translated into Japanese
"""

from local_settings import DEEPL_APIKEY
import requests


class DeepL:
    def __init__(self):
        """Creates an empty string instance to save the translated text."""
        self.translated_text = ""

    def translate(self, text):
        """Translates the stt text using the DeepL API (From English to Japanese).

        Args:
            text (string): string of transcribed content from stt.

        Returns:
            translated_text: string of Japanese text translated using DeepL.
        """
        TEXT = text
        params = {
            "auth_key": DEEPL_APIKEY,
            "text": TEXT,
            "source_lang": "EN",
            "target_lang": "JA",
        }

        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        self.translated_text = result["translations"][0]["text"]
        return self.translated_text
