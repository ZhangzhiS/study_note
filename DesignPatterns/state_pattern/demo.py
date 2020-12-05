#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from abc import abstractmethod, ABCMeta


class Coffee(metaclass=ABCMeta):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_taste(self):
        pass


class LatteCoffee(Coffee):

    def __init__(self, name):
        super().__init__(name)

    def get_taste(self):
        return "轻柔醇香"


class Coffeemaker:

    @staticmethod
    def make_coffee(coffee_bean):
        if coffee_bean == 1:
            coffee = LatteCoffee(1)
        else:
            raise ValueError("coffee bean not supported")
        return coffee


if __name__ == '__main__':
    latte = Coffeemaker.make_coffee(1)
    print(latte.get_taste())