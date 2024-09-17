
# 2. Реализовать проект расчета ...

from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def tissue(self):
        assert False, f'Этот метод дожен быть доопределен в подклассах.' \
            f' Если поиск в метода в дереве наследованя дошел до этого места значит этого не случилось.'
                      # из-за декоратора abstractmethod - исключение assert не сработает;
                      # abstractmethod перехватит ошибку.
class Coat(Cloth):

    def __init__(self, v):
        self.size = v
    @property
    def tissue(self):
        return round(self.size / 6.5 + .5, 1)

class Suit(Cloth):

    def __init__(self, h):
        self.height = h
    # @property
    def tissue(self):
        return round(self.height * 2 + .3, 1)

if __name__ == '__main__':
    c = Coat(50)
    print(c.size)
    # print(c.tissue())
    print(c.tissue)
    print('')
    s = Suit(180)
    print(s.height)
    print(s.tissue())
    # print(s.tissue)
