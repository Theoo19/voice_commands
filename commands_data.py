from time import localtime
from weather import Weather
import wikipedia


class Data:
    __weather = Weather()
    __default_place = "the hague"
    __months = {1: "january",
                2: "february",
                3: "march",
                4: "april",
                5: "may",
                6: "june",
                7: "july",
                8: "august",
                9: "september",
                10: "october",
                11: "november",
                12: "december"}

    @staticmethod
    def date():
        year, month, day = localtime()[:3]
        return "It's {} {} {}".format(day, Data.__months[month], year)

    @staticmethod
    def time():
        hour, minute = localtime()[3:5]
        if hour < 10:
            hour = "0{}".format(hour)
        if minute < 10:
            minute = "0{}".format(minute)
        return "It's {}:{} o'clock".format(hour, minute)

    @staticmethod
    def temperature(name):
        if "in" in name:
            index = name.index("in")
            name = " ".join(name[index + 1:])
        else:
            name = Data.__default_place
        print(name)
        try:
            place = Data.__weather.lookup_by_location(name)
            celcius = round((float(place.condition().temp()) - 32) / 1.8, 1)
            return "It's {} degrees celcius in {}.".format(celcius, name)
        except AttributeError:
            return "It looks like {} doesn't exist.".format(name)

    @staticmethod
    def information(subject):
        try:
            subject = wikipedia.summary(" ".join(subject), sentences=2)
            return subject
        except wikipedia.exceptions.PageError:
            return "There doesn't exist any page about that subject. Please try again."
        except wikipedia.exceptions.DisambiguationError:
            return "There seem to be multiple subjects. Please be more specific."
