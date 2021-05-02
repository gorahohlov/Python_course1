# 7.-----------------------------------

def fact(ar_1):
    for gen in range(1, ar_1 + 1):
        yield gen

a = 1
n = int(input('Введите натуральное число: '))
for el in fact(n):
    a *= el
    print(f'Факториал {el}! равен: {a}')
