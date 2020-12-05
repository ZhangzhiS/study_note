#!/usr/bin/env python3.8
from abc import abstractmethod


class WaterHeater:
    """
    热水器
    """
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print(f"当前温度是{self.__temperature}℃")
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer:

    @abstractmethod
    def update(self, water_heater):
        pass


class WashingMode(Observer):
    """该模式用于洗澡用"""

    def update(self, water_heater):
        if 50 <= water_heater.get_temperature() < 70:
            print("水已烧好，温度正好！可以用来洗澡了。")


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print("水已烧开！可以用来饮用了。")


if __name__ == '__main__':
    heater = WaterHeater()
    washing_obser = WashingMode()
    drinking_obser = DrinkingMode()
    heater.add_observer(washing_obser)
    heater.add_observer(drinking_obser)
    heater.set_temperature(40)
    heater.set_temperature(65)
    heater.set_temperature(100)
