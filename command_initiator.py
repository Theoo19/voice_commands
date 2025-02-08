from .command_selector import SetParamCommand, NewParamCommand, NoParamCommand, Command
from .commands_control import Program, Google
from .commands_sound import Sound
from .commands_data import Data
from .commands_math import Math
from .responses import Basic

Command = Command
Sound.setup_volume()
# ==========================

NewParamCommand(Program.open, first_words=["open", "start"])
NewParamCommand(Program.close, first_words=["stop"])
# ==========================

NewParamCommand(Google.search, first_words=["google", "zoek"])
NewParamCommand(Google.maps, first_words=["maps", "waar is", "waar ligt"])
# ==========================

NoParamCommand(Sound.volume_up, key_words=["volume omhoog"])
NoParamCommand(Sound.volume_down, key_words=["volume omlaag"])
NewParamCommand(Sound.volume_set, key_words=["zet het volume op"], combined_words=[["zet", "volume"]])
NoParamCommand(Sound.mute, key_words=["demp"],
               combined_words=[["geluid", "aan"], ["geluid", "uit"], ["volume", "aan"], ["volume", "uit"]])
# ==========================

NoParamCommand(Data.date, key_words=["datum", "vandaag"], combined_words=[["welke", "dag"]])
NoParamCommand(Data.time, key_words=["tijd"], combined_words=[["hoe", "laat"]])
NewParamCommand(Data.temperature, key_words=["temperatuur", "celcius"],
                combined_words=[["hoe", "warm"], ["hoe", "koud"], ["hoeveel", "graden"]])
NewParamCommand(Data.information, key_words=["informatie"], first_words=["wie is", "wat is"])
# Difficult function. See end of this page for more info.
# ==========================

NewParamCommand(Math.add,       key_words=["plus"])
NewParamCommand(Math.subtract,  key_words=["min"])
NewParamCommand(Math.multiply,  key_words=["keer"])
NewParamCommand(Math.divide,    combined_words=[["gedeeld", "door"], ["delen", "door"], ["deel", "door"]])
NewParamCommand(Math.square,    key_words=["kwadraat"])
NewParamCommand(Math.squareroot, key_words=["wortel"])
NewParamCommand(Math.random,    key_words=["willekeurig"])
# ==========================

SetParamCommand(Basic.macro,    parameters=["control", "c"], key_words=["kopieer"])
SetParamCommand(Basic.macro,    parameters=["control", "v"], key_words=["plak"])
SetParamCommand(Basic.macro,    parameters=["control", "left_win", "d"], combined_words=[["nieuw", "bureaublad"]])
SetParamCommand(Basic.macro,    parameters=["control", "left_win", "f4"], combined_words=[["sluit", "bureaublad"]])
SetParamCommand(Basic.macro,    parameters=["control", "left_win", "left"],
                combined_words=[["linker", "bureaublad"], ["links", "bureaublad"]])
SetParamCommand(Basic.macro,    parameters=["control", "left_win", "right"],
                combined_words=[["rechter", "bureaublad"], ["rechts", "bureaublad"]])

SetParamCommand(Basic.say,      parameters=["hey", "hello", "how are you"],
                key_words=["hallo", "hoi", "hai", "hey", "hi"])
SetParamCommand(Basic.say,      parameters=["goodbye", "bye", "see you"], key_words=["doei", "tot ziens"])
# ==========================
