
# 1. Реализовать класс Matrix...

class Matrixes:
    def __init__(self, mt=None):
        if mt is None:
            print('Для окончания ввода матрицы введите q или пустую строку')
            m = []
            while True:
                k = input('Вводите через пробел числа - строки матрицы: \n').split()
                if k == [] or k == ['q']:
                    break
                m.append([int(i) for i in k])
            self.mtrx = m
        else:
            self.mtrx = mt

    # вариант 1 /с постоянной длиной каждого элемента/
    # def __str__(self):
    #     prn = ''
    #     for i in self.mtrx:
    #         prn += f"|{' '.join([str(k) for k in i])}|\n"
    #     return prn

    # вариант 2 /с учетом разрядности элементов, переменная длина элементов/
    def __str__(self):
        ddd = 0  # максимальная разрядность элемента, для выравнивания границ матрицы
        for k in self.mtrx:
            for n in k:
                ddd = max(ddd, len(str(n)))
        prn_clmn = ''
        for i in self.mtrx:
            prn_line = '|'
            for j in i:
                prn_line += f"{j:>{ddd}} "
            prn_line = prn_line[:-1] + '|\n'
            prn_clmn += prn_line
        return prn_clmn

    def __add__(self, other):
        ln, m = [], []
        for k in range(0, len(self.mtrx)):
            for n in range(0, len(self.mtrx[0])):
                ln.append(self.mtrx[k][n] + other.mtrx[k][n])
            m.append(ln)
            ln = []
        return Matrixes(m)


if __name__ == '__main__':
    mt1 = Matrixes([[1, 22], [333, 4444]])
    print(mt1)
    mt2 = Matrixes([[55555, 666666], [7777777, 88888888]])
    print(mt2)
    print(mt1 + mt2)
    mt3 = Matrixes()
    print(mt3)
