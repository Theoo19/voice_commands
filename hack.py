from keyboard import Keyboard
from time import sleep


def new():
    for x in range(5):
        Keyboard.key("backspace")


def enter():
    Keyboard.key("enter")


def caps_lock():
    Keyboard.key("capital")


for x in range(5):
    print("{}...".format(x))
    sleep(1)

for year in range(1900, 2000):
    Keyboard.text(str(year))
    enter()
    new()
