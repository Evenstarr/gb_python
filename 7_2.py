from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_size(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def cloth_size(self):
        return self.v/6.5 + 0.5

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 40:
            self.__v = 40
        elif v > 65:
            self.__v = 65
        else:
            self.__v = v


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def cloth_size(self):
        return self.h * 2 + 0.3

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1.5:
            self.__h = 1.5
        elif h > 2.1:
            self.__h = 2.1
        else:
            self.__h = h


coat = Coat(50)
suit = Suit(1.7)

print(f'{2*coat.cloth_size + 3*suit.cloth_size:0.2f}')
