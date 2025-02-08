from .commands_math import Number


class Command:
    __all = list()

    @staticmethod
    def add(command):
        Command.__all.append(command)

    @staticmethod
    def run(command, parameters):
        if type(command) is SetParamCommand or type(command) is NoParamCommand:
            return command.execute()
        parameters = list(Number.from_string(item) for item in parameters)
        return command.execute(parameters)

    @staticmethod
    def selector(string):
        string = string.lower()
        current_command = None
        parameters = str()

        for command in Command.__all:
            for first_word in command.first_words:
                if string.startswith(first_word):
                    parameters = string.replace(first_word, "").split()
                    current_command = command
                    break
            if current_command is not None:
                break

        if current_command is None:
            for command in Command.__all:
                for key_word in command.key_words:
                    if key_word in string:
                        parameters = string.replace(key_word, "").split()
                        current_command = command
                        break
                if current_command is not None:
                    break

        if current_command is None:
            string_list = string.split()
            for command in Command.__all:
                for combined_words in command.combined_words:
                    if all(word in string_list for word in combined_words):
                        parameters = list(word for word in string_list if word not in combined_words)
                        current_command = command
                        break
                if current_command is not None:
                    break

        if current_command is not None:
            return Command.run(current_command, parameters)
        return "I'm sorry, that doesn't sound like something I can do."


class SetParamCommand(Command):
    def __init__(self, func, parameters, key_words=list(), first_words=list(), combined_words=list()):
        self.parameters = parameters
        self.function = func
        self.key_words = key_words
        self.first_words = first_words
        self.combined_words = combined_words
        Command.add(self)

    def execute(self):
        return self.function(*self.parameters)


class NewParamCommand(Command):
    def __init__(self, func, key_words=list(), first_words=list(), combined_words=list()):
        self.function = func
        self.key_words = key_words
        self.first_words = first_words
        self.combined_words = combined_words
        Command.add(self)

    def execute(self, parameters=str()):
        return self.function(parameters)


class NoParamCommand(Command):
    def __init__(self, func, key_words=list(), first_words=list(), combined_words=list()):
        self.function = func
        self.key_words = key_words
        self.first_words = first_words
        self.combined_words = combined_words
        Command.add(self)

    def execute(self):
        return self.function()
