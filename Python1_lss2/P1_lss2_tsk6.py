#6 ----------------------------------

n = 1
lst = []
dct, d1 = {}, {}
tpl = ()
a, a1 = ' ', ''
while True:
    print('-'*20)
    print(f'Введите данные для товара №: {n} или нажмите Enter для завершения')
    a = input(f'Введите название товара {n}: ')
    if a == '':
        break
    dct = dict(название = a)
    a1 = input(f'Введите цену товара {n}: ')
    d1 = dict(цена = int(a1))
    dct.update(d1)
    a1 = input(f'Введите количество товара {n}: ')
    d1 = dict(количество = int(a1))
    dct.update(d1)
    a1 = input(f'Введите единицу измерения товара {n}: ')
    d1 = dict(ед = a1)
    dct.update(d1)
    tpl = (n, dct)
    lst.append(tpl)
    n += 1
print('Введенный список значений: \n')
print('[')
for i in lst:
    print(i, ',')
print(']')


# lst = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт'})]

d2 = {}
ls_name, ls_prc, ls_qty, ls_ea = [], [], [], []
for i in lst:
    ls_name.append(i[1].get('название'))
    ls_prc.append(i[1].get('цена'))
    ls_qty.append(i[1].get('количество'))
    ls_ea.append(i[1].get('eд'))
d2 = dict(название = list(set(ls_name)))
d2['цена'] = list(set(ls_prc))
d2['количество'] = list(set(ls_qty))
d2['ед'] = list(set(ls_ea))
print(d2)
print('-'*20)
for j in d2:
    print(j, ':', d2.get(j), ',')