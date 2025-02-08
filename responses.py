from .keyboard import Keyboard
from random import choice
from time import sleep

class Basic:
    @staticmethod
    def macro(*keys):
        for key in keys:
            Keyboard.key_down(key)
        for key in keys:
            Keyboard.key_up(key)

    @staticmethod
    def key_stream(*keys):
        for key in keys:
            Keyboard.key(key)

    @staticmethod
    def say(*sentences):
        return choice(sentences)
