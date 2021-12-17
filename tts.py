"""Receives the translated text to DeepL and creates an mp3 file of the text using the IBM Watson text to speech module.
"""

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from local_settings import IBM_WATSON_APIKEY
import playsound
import os
import time


class TextToSpeech:
    def speak(self, text):
        """Uses the the text to speech module from IBM Watson to create an .mp3 file of the tranlsated text.
        The file is then played using playsound, and is then deleted to conserve storage.

        Args:
            text: translated text from DeepL
        """
        url = "https://api.jp-tok.text-to-speech.watson.cloud.ibm.com/instances/a48525e6-b3bf-49d7-9858-2b99372a345b"
        authentication = IAMAuthenticator(IBM_WATSON_APIKEY)
        tts = TextToSpeechV1(authenticator=authentication)
        tts.set_service_url(url)

        with open("./sample.mp3", "wb") as audio_file:
            res = tts.synthesize(
                text=text, accept="audio/mp3", voice="ja-JP_EmiV3Voice"
            ).get_result()
            audio_file.write(res.content)
            playsound.playsound("./sample.mp3")

        now = time.time()
        path = "./sample.mp3"
        os.remove(path)
