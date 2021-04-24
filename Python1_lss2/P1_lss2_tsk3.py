#3 ----------------------------------

li = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
il = input('Введите номер месяца: ')
if il.isnumeric() == False:
    print('Введены некорректные данные. Введети целое число от 1 до 12.')
else:
    print(li[int(il)-1])

li = ['зима', 'весна', 'лето', 'осень']
il = input('Введите номер месяца: ')
if il.isnumeric() == False:
    print('Введены некорректные данные. Введети целое число от 1 до 12.')
else:
    il = int(il)
    if il == 1 or il == 2 or il == 12:
        print(li[0])
    elif il == 3 or il == 4 or il == 5:
        print(li[1])
    elif il == 6 or il == 7 or il == 8:
        print(li[2])
    else:
        print(li[3])

seas = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
il = input('Введите номер месяца: ')
if il.isnumeric() == False:
    print('Введены некорректные данные. Введети целое число от 1 до 12.')
else:
    if il == '1' or il == '2' or il == '12':
        print(seas.get(1))
    elif il == '3' or il == '4' or il == '5':
        print(seas.get(2))
    elif il == '6' or il == '7' or il == '8':
        print(seas.get(3))
    else:
        print(seas.get(4))