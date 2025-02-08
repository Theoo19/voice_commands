from .commands_math import Number


class Dict:
    @staticmethod
    def from_txt(filename):
        dictionary = dict()
        if not filename.endswith(".txt"):
            filename += ".txt"
        with open(filename, "r") as file:
            content = file.read().split("\n")
        for item in content:
            item = item.split(": ")
            dictionary[item[0]] = Number.from_string(item[1])
        return dictionary

    @staticmethod
    def add_key(dictionary, key, value, filename):
        dictionary[key] = value
        if not filename.endswith(".txt"):
            filename += ".txt"
        with open(filename, "a") as file:
            file.write("\n{} {}".format(key, value))
