
# 3. Создайте собственный класс-исключение, который должен
# проверять содержимое списка на наличие только чисел

class IsNumb(Exception):

    @staticmethod
    def raiser_1(param_1):
        try:
            if param_1.isdigit():
                return int(param_1)
            else:
                float(param_1)
                return float(param_1)
        except ValueError:
            return False

ls = []
while True:
    x = input('Введите число. Для завершения заполнения списка числами введите stop: ')
    if x == 'stop':
        break
    else:
        y = IsNumb.raiser_1(x)
        if y is False:
            print('Введенный элемент не число!')
            continue
        else:
            ls.append(y)
print(ls)
