# 1. -------------------------------

def div_1():
    dvnt = float(input('Введите делимое: '))
    dvsr = float(input('Введите делитель: '))
    try:
        # dvnt / dvsr
        return dvnt / dvsr
    except:
        return print('Операция не может быть выполнена. Ошибка деление на ноль!')

print(div_1())

# -------------------------------

a_1 = input('Введите делимое: \n')
a_2 = input('Введите делитель: \n')
def div_2(ar_1, ar_2):
    try:
        ar_1, ar_2 = float(ar_1), float(ar_2)
        return ar_1 / ar_2
    except ValueError:
        return 'Операнды не числа. Введите числа.'
    except ZeroDivisionError:
        return print('Ошибка деления на ноль! Укажите другой делитель.')

print(div_2(a_1, a_2))
