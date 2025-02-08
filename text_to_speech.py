import win32com.client
import speech_recognition as sr


with open("service-account.json", "r") as file:
    credentials = file.read()


class Voice:
    __voice = win32com.client.Dispatch("SAPI.SpVoice")
    __recorder = sr.Recognizer()

    @staticmethod
    def say(*string):
        string = " ".join(list(str(item) for item in string))
        Voice.__voice.Speak(string)

    @staticmethod
    def listen():
        with sr.Microphone() as source:
            audio = Voice.__recorder.listen(source, phrase_time_limit=5)
        return audio

    @staticmethod
    def recognize(audio, language="nl-NL"):
        try:
            return Voice.__recorder.recognize_google(audio, language=language).lower()
        except sr.UnknownValueError:
            raise VoiceError

    @staticmethod
    def recognize_cloud(audio, language="nl-NL"):
        try:
            return Voice.__recorder.recognize_google_cloud(audio, language=language, credentials_json=credentials)
        except sr.UnknownValueError:
            raise VoiceError


class VoiceError(Exception):
    pass
