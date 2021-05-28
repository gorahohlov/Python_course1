
# 2. Создать собственный клас исключение

class Errr(Exception):
    def __init__(self):
        self.messge = 'Операция деления на ноль не поддерживается'

    @staticmethod
    def raiser0():
        # global b
        while True:
            b = int(input('Ввдедите число-делитель отличное от нуля: '))
            if b != 0:
                print(f'Результат: {a / b}')
                break
            else:
                print('Вы ввели делитель равный нулю. Попробуйте снова.')

a, b = 12, 0

try:
    a / b
except ZeroDivisionError:
    e = Errr()
    print(e.messge)
    Errr.raiser0()
    e.raiser0() # как вариант вызова, тоже работает
else: print(f'Результат: {a / b}')
