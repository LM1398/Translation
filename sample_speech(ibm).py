import speech_recognition as sr
import requests
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time
import os
import playsound
from local_settings import DEEPL_APIKEY, IBM_WATSON_APIKEY

r1 = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        # settings up variables
        # microphone as source
        # sends the sound to google API for speech recognition (slow)
        print("Please Speak now: ")
        r1.energy_threshold = 61.63
        r1.adjust_for_ambient_noise(source, duration=0.5)
        audio = r1.listen(source)
        text = r1.recognize_google(audio, language="en-US")

        print(text)

        # Using DeepL translation to translate the text from speech recognition
        TEXT = text
        params = {
            "auth_key": DEEPL_APIKEY,
            "text": TEXT,
            "source_lang": "EN",
            "target_lang": "JA",
        }

        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        translated = result["translations"][0]["text"]

        # prints the text from r1 as well as text from deepL

        print(translated)

        # # Using IBM watson text to speech

        url = "https://api.jp-tok.text-to-speech.watson.cloud.ibm.com/instances/a48525e6-b3bf-49d7-9858-2b99372a345b"
        authentication = IAMAuthenticator(IBM_WATSON_APIKEY)
        tts = TextToSpeechV1(authenticator=authentication)
        tts.set_service_url(url)

        with open("./sample.mp3", "wb") as audio_file:
            res = tts.synthesize(
                text=translated, accept="audio/mp3", voice="ja-JP_EmiV3Voice"
            ).get_result()
            audio_file.write(res.content)
            playsound.playsound("./sample.mp3")

        now = time.time()
        path = "./sample.mp3"
        os.remove(path)
        while True:
            current_time = time.time()
            if current_time - now > 0:
                break

        if text == "quit":
            break
