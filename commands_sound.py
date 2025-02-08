from .keyboard import Keyboard
from .commands_math import Number


class Sound:
    __standard_volume = 20
    __current_volume = 100
    __muted = False

    @staticmethod
    def setup_volume():
        Sound.volume_min()
        Sound.volume_set(Sound.__standard_volume)

    @staticmethod
    def current_volume():
        return Sound.__current_volume

    @staticmethod
    def is_muted():
        return Sound.__muted

    @staticmethod
    def mute():
        if not Sound.__muted:
            Sound.__muted = True
            Keyboard.key("volume_mute")

    @staticmethod
    def unmute():
        if Sound.__muted:
            Sound.__muted = False
            Keyboard.key("volume_mute")

    @staticmethod
    def change_mute_stage():
        Sound.__muted = not Sound.__muted
        Keyboard.key("volume_mute")

    @staticmethod
    def volume_up():
        if Sound.__current_volume <= 98:
            Sound.__current_volume += 2
            Keyboard.key("volume_up")

    @staticmethod
    def volume_down():
        if Sound.__current_volume >= 2:
            Sound.__current_volume -= 2
            Keyboard.key("volume_down")

    @staticmethod
    def volume_set(amount):
        if type(amount) is not int:
            amount = Number.get(amount)[0]
        if Sound.__current_volume > amount:
            for i in range(0, int((Sound.__current_volume - amount) / 2)):
                Sound.volume_down()
        elif Sound.__current_volume == amount:
            pass
        else:
            for i in range(0, int((amount - Sound.__current_volume) / 2)):
                Sound.volume_up()

    @staticmethod
    def volume_min():
        Sound.volume_set(0)

    @staticmethod
    def volume_max():
        Sound.volume_set(100)
