
# 3. Работа с органическими клетками ...

class Cellula:

    def __init__(self, q):
        self.qty = q

    def __add__(self, other):
        # return Cellula(self.qty + other.qty).qty
        return Cellula(self.qty + other.qty)

    def __sub__(self, other):
        return Cellula(self.qty - other.qty)

    def __mul__(self, other):
        return Cellula(self.qty * other.qty)

    def __truediv__(self, other):
        return Cellula(int(round(self.qty / other.qty, 0)))

    def make_order(self, n):
        if self.qty // n != 0:
            a = ('*' * n + '\\n') * (self.qty // n) + '*' * (self.qty % n)  # + '.'
        else:
            a = '*' * self.qty  # + '.'
        # return a[:-3] + '.' if self.qty % n == 0 else a
        # я не понял точка в конце нужно или нет. Но это же неважно)))
        return a[:-2] if self.qty % n == 0 else a


if __name__ == '__main__':
    cell_1 = Cellula(6)
    cell_2 = Cellula(8)
    print(cell_1 + cell_2)
    cell_3 = cell_1 + cell_2
    print(cell_3.qty)
    print((cell_1 + cell_2).qty)
    print('')
    print((cell_2 - cell_1).qty)
    cell_4 = cell_2 - cell_1
    print(cell_4.qty)
    print('')
    cell_5 = cell_1 * cell_2
    print(cell_5.qty)
    print('')
    cell_6 = Cellula(24) / cell_1
    print(cell_6.qty)
    print((Cellula(36) / Cellula(12)).qty)

    cell_7 = Cellula(4)
    a = (Cellula.make_order(cell_7, 6))
    print(a)
    print(Cellula.make_order(Cellula(12), 5))
