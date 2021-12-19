"""Main Python file used to combine: speech to text -> translation to Japanese -> text to speech.
"""

from stt import SpeechToText
from deepl import DeepL
from tts import TextToSpeech
import time


def main():
    stt = SpeechToText()
    deepl = DeepL()
    tts = TextToSpeech()

    while True:
        stt.transcribe()
        print(str.capitalize(stt.text))
        if stt.text == "quit":
            print("\nQuitting...")
            break
        deepl.translate(stt.text)
        print(deepl.translated_text)
        tts.speak(deepl.translated_text)
        now = time.time()
        while True:
            current_time = time.time()
            if current_time - now > 0:
                break


if __name__ == "__main__":
    main()
