"""Receives the translated text to DeepL and creates an mp3 file of the text using the IBM Watson text to speech module.
"""

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from local_settings import IBM_WATSON_APIKEY
import playsound
import os
import yaml
import time

with open("./envs/config.yml") as file:
    config = yaml.safe_load(file.read())


class TextToSpeech:
    def speak(self, text):
        """Uses the the text to speech module from IBM Watson to create an .mp3 file of the tranlsated text.
        The file is then played using playsound, and is then deleted to conserve storage.

        Args:
            text: translated text from DeepL
        """
        url = config["ibm_watson_url"]
        authentication = IAMAuthenticator(IBM_WATSON_APIKEY)
        tts = TextToSpeechV1(authenticator=authentication)
        tts.set_service_url(url)

        tmp_file = "./sample.mp3"  # Temporary mp3 file created throught the api that is then played using playsound.
        with open(tmp_file, "wb") as audio_file:
            res = tts.synthesize(
                text=text, accept=config["accepted_file_type"], voice=config["voice"]
            ).get_result()
            audio_file.write(res.content)
            playsound.playsound(tmp_file)

        path = "./sample.mp3"
        os.remove(path)
