
# 7. Реализовать проект «Операции с комплексными числами».

from math import atan2

class Cmplx:
    def __init__(self, a, b):   # не буду заморачиваться инициализацией комплексного числа
        self.rl = a             # через строковый литерал Cmpx('a+bj') ограничусь таким способом;
        self.im = b
    def __str__(self):
        if self.rl == 0:
            return f'{self.im}j'
        else:
            return f'({self.rl}{"+" if self.im >= 0 else ""}{self.im}j)'
    def __add__(self, other):
        return Cmplx((self.rl + other.rl), (self.im + other.im))
    def __sub__(self, other):
        return Cmplx((self.rl - other.rl), (self.im - other.im))
    def __mul__(self, other):
        if type(self) is not Cmplx or type(other) is not Cmplx:
            return f'Ошибка типа. Введите операнды как экземпляры класса Cmplx'
        else:
            return Cmplx((self.rl * other.rl - self.im * other.im), (self.rl * other.im + self.im * other.rl))
    def md(self): # модуль комплексного числа
        return (self.rl ** 2 + self.im ** 2) ** .5
    def ar(self): # аргумент
        return atan2(self.im, self.rl)

if __name__ == '__main__':
    z1 = Cmplx(1, 6)
    print(z1)
    z2 = Cmplx(4, 8)
    print(z2)
    print('------')
    print(f'z1: ({z1.rl}+{z1.im}j); z2: ({z2.rl}+{z2.im}j)')
    print('------')
    z3 = Cmplx(0, 1)
    print(z3)
    z4 = Cmplx(6, 0)
    print(z4)
    print('------')
    z5 = z1 + z2
    print(z5)
    print(z1 + z2)
    print('ok' if type(z5) is Cmplx else '!ok')
    z6 = 1
    print('ok' if type(z6) is Cmplx else '!ok')
    print(type(z6) is Cmplx)
    print(z1 * z2)
    print(z2 - (z5 + z1))
    print(f'{z5} модуль: {z5.md()}')
    print(f'{z5} аргумент: {z5.ar()}')