import subprocess
import webbrowser
import os
from .dictionary import Dict
programs_path = "\Shortcuts"


class Program:
    __standard_websites = Dict.from_txt("standard websites")
    __standard_programs = list(file[:-4] for file in os.listdir(programs_path))
    __standard_tasks = Dict.from_txt("standard tasks")
    __active_tasks = set()

    @staticmethod
    def open(name):
        if len(name) == 0:
            raise TypeError
        name = " ".join(str(item) for item in name)
        if name.startswith("www."):
            webbrowser.open(name)
        elif name.endswith((".nl", ".com", ".net")):
            webbrowser.open("www.{}".format(name))
        elif name in Program.__standard_websites:
            webbrowser.open(Program.__standard_websites[name])
        elif name in Program.__standard_programs:
            os.startfile("{}\{}".format(programs_path, name))
        elif name.replace(" ", "") in Program.__standard_programs:
            os.startfile("{}\{}".format(programs_path, name.replace(" ", "")))
        else:
            return "I'm sorry, I couldn't find: \"{}\".".format(name)
        return "Successfully opened: \"{}\"".format(name)

    @staticmethod
    def close(name):
        if len(name) == 0:
            quit()
        results = set()
        name_1 = " ".join(str(item) for item in name)
        name_2 = "".join(str(item) for item in name)

        for task in Program.all_tasks():
            task_name = task[:-4].lower()
            if task_name in name_1 or task_name in name_2 or name_1 in task_name or name_2 in task_name:
                command = "taskkill /IM {} /T /F".format(task)
                results.add(subprocess.run(command, stdout=subprocess.PIPE).stdout.decode()[:6].lower())

        if "success" not in results:
            return "I'm sorry, I couldn't find: \"{}\".".format(name_1)
        return "Successfully closed: \"{}\"".format(name_1)

    @staticmethod
    def update_tasks():
        tasks = set(task.split()[0] for task in subprocess.check_output("tasklist").decode().split("\r\n")[3:])
        Program.__active_tasks = tasks

    @staticmethod
    def all_tasks():
        Program.update_tasks()
        return Program.__active_tasks


class Google:
    __modes = {"google": "https://www.google.nl/search?q=",
               "maps": "https://www.google.nl/maps/place/",
               "wiki": "https://nl.wikipedia.org/wiki/"}

    @staticmethod
    def open(mode, name):
        if len(name) == 0:
            raise TypeError
        mode = Google.__modes[mode]
        name = " ".join(str(item) for item in name)
        webbrowser.open("{}{}".format(mode, name))

    @staticmethod
    def search(name):
        Google.open("google", name)

    @staticmethod
    def maps(name):
        Google.open("maps", name)

    @staticmethod
    def wiki(name):
        Google.open("wiki", name)
