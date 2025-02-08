from math import sqrt, pow
from random import randint


class Number:
    @staticmethod
    def from_string(string):
        if string.isdigit():
            return int(string)
        else:
            try:
                return float(string.replace(",", "."))
            except ValueError:
                return string

    @staticmethod
    def get(iterable):
        numbers = list(item for item in iterable if type(item) is int or type(item) is float)
        return numbers


class Math:
    @staticmethod
    def add(numbers):
        result = 0
        for number in Number.get(numbers):
            result += number
        return result

    @staticmethod
    def subtract(numbers):
        numbers = Number.get(numbers)
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
        return result

    @staticmethod
    def multiply(numbers):
        result = 1
        for number in Number.get(numbers):
            result *= number
        return result

    @staticmethod
    def divide(numbers):
        numbers = Number.get(numbers)
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
        return result

    @staticmethod
    def square(number):
        number = Number.get(number)[0]
        return pow(number, 2)

    @staticmethod
    def power(numbers):
        numbers = Number.get(numbers)
        number = numbers[0]
        power = numbers[1]
        return pow(number, power)

    @staticmethod
    def squareroot(number):
        number = Number.get(number)[0]
        return sqrt(number)

    @staticmethod
    def random(numbers):
        numbers = Number.get(numbers)
        if len(numbers) == 0:
            range_1, range_2 = 0, 100
        elif len(numbers) == 1:
            range_1, range_2 = 0, numbers[0]
        else:
            range_1, range_2 = numbers[0], numbers[1]
        return randint(range_1, range_2)
