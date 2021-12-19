"""Contains speech to text portion of translation module.
"""


import speech_recognition as sr
import yaml

with open("./envs/config.yml") as file:
    config = yaml.safe_load(file.read())


class SpeechToText:
    def __init__(self):
        """Creates an empty string instance to save the transcribed text."""
        self.text = ""

    def transcribe(self):
        """Uses speech recognition to record mic audio, and uses the Google speech to text API to translate it into text.

        Returns:
            text: string of transcribed text.
        """
        with sr.Microphone() as source:
            r1 = sr.Recognizer()
            print("\nPlease Speak now: ")
            r1.energy_threshold = config["mic_energy_threshold"]
            r1.adjust_for_ambient_noise(source, duration=config["mic_duration"])
            audio = r1.listen(source)
            self.text = r1.recognize_google(audio, language=config["google_language"])
        return self.text
