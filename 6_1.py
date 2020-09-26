from termcolor import colored
from time import sleep
from itertools import cycle


class TrafficLight:
    __color = "red"

    def running(self):
        # Вообще время по идее надо выносить в аттрибуты, и не просто в аттрибуты, а задавать при создании. Но в условии
        # этого нет, поэтому здесь
        colors = {"red": 7, "yellow": 2, "green": 5}
        tmp = cycle(colors.keys())
        while True:
            self.__color = next(tmp)
            print(colored(self.__color, self.__color))
            sleep(colors[self.__color])


tl = TrafficLight()
tl.running()
