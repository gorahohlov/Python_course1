
# 1. Реализовать класс 'data' ...

# 1.1 вариант: предполагается формат ввода даты 'dd-mm-yyyy'
class DDate:

    def __init__(self, dmy):
        self.dte = dmy

    @classmethod
    def cnvrt(cls, dmy):
        d = int(dmy[:2])
        m = int(dmy[3:5])
        y = int(dmy[-4:])
        DDate.vld_method(d, m, y)

    @staticmethod
    def vld_method(a1, a2, a3):
        a = 0
        if a3 < 0:
            print(f'Год не может быть меньше нуля! Год: {a3}')
            a += 1
        if a2 not in range(1, 13):
            print(f'Значение месяца не может быть больше 12 и меньше 1! Месяц#: {a2}')
            a += 1
        if a1 > 31: print(f'Количество дней в месяце не может превышать 31! Дней#: {a1}')
        if a2 in (1, 3, 5, 7, 8, 10, 12) and a1 not in range(1, 32):
            print(f'число дней не может превышать 31! Дней#: {a1}, Месяц#: {a2}')
            a += 1
        if a2 in (4, 6, 9, 11) and a1 not in range(1, 31):
            print(f'число дней не может превышать 30! Дней#: {a1}, Месяц#: {a2}')
            a += 1
        if a2 == 2 and a1 not in range(1, 30):
            print(f'число дней в феврале не может превышать 29! Дней#: {a1}, Месяц#: {a2}')
            a += 1
        if a == 0: print(f'{a1:02}/{a2:02}/{a3:04}')
        print('-'*12)

if __name__ == '__main__':
    print('*'*16)
    DDate.cnvrt('41-13-1900')
    print('*'*16)
    DDate.cnvrt('08-10-2014')
    print('*' * 16)
    dt = DDate('09-03-2005')
    dt.cnvrt(dt.dte)