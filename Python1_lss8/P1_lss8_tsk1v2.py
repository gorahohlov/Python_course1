
# 1. Реализовать класс 'data' ...

# 1.2 вариант: формат ввода даты может быть 'd-m-yy', 'dd-m-yy', 'd-mm-yyyy' ...
# можно, как вариант в конструкции if ... elif ... else
# - тогда будет выдаваться только одна (первая ошибка)

class DDate:

    def __init__(self, dmy):
        self.dte = dmy

    @classmethod
    def cnvrt(cls, dmy):
        x = dmy.split('-')
        d = int(x[0])
        m = int(x[1])
        y = int(x[2])
        DDate.vld_method(d, m, y)

    @staticmethod
    def vld_method(a1, a2, a3):
        if a3 < 100:
            if a3 <= 36:
                a3 = 2000 + a3
            else:
                a3 = 1900 + a3
        if a3 < 0:
            print(f'Год не может быть меньше нуля! Год: {a3}')
        elif a1 > 31: print(f'Количество дней в месяце не может превышать 31! Дней#: {a1}')
        elif a2 not in range(1, 13):
            print(f'Значение месяца не может быть больше 12 и меньше 1! Месяц#: {a2}')
        elif a2 in (1, 3, 5, 7, 8, 10, 12) and a1 not in range(1, 32):
            print(f'число дней не может превышать 31! Дней#: {a1}, Месяц#: {a2}')
        elif a2 in (4, 6, 9, 11) and a1 not in range(1, 31):
            print(f'число дней не может превышать 30! Дней#: {a1}, Месяц#: {a2}')
        elif a2 == 2 and a1 not in range(1, 30):
            print(f'число дней в феврале не может превышать 29! Дней#: {a1}, Месяц#: {a2}')
        # else: print(f'{a1:02}/{a2:02}/{2000 + a3 if a3 <= 36 else 1900 + a3:04}')
        else: print(f'{a1:02}/{a2:02}/{a3:04}')


if __name__ == '__main__':
    print('*'*16)
    DDate.cnvrt('41-13-1900')
    print('*'*16)
    DDate.cnvrt('08-10-2014')
    print('*' * 16)
    dt = DDate('09-03-2005')
    dt.cnvrt(dt.dte)
    print('*' * 16)
    DDate.cnvrt('9-3-05')
    print('*' * 16)
    DDate.cnvrt('8-10-2014')
    print('*' * 16)
    DDate.cnvrt('28-11-77')
    print('*' * 16)
