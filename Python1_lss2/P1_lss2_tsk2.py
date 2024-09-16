#2 ----------------------------------

#ls = input('Введите значения списка')
print('Вводите элементы списка; по окончании введите Enter!')
ls = []
a = ' '
while a != '':
    a = input('Введите следующй элемент списка или нажмите Enter: ')
    if a != '':
        if a.isnumeric() == False:
            ls.append(a)
            continue
        try:
            type(int(a)) == int
            ls.append(int(a))
            continue
        except:
            type(float(a)) == float
            ls.append(float(a)) # не смог добиться изменения типа для float;
                                # контринуитивно для float .isnumerinc() выдает False %) либо возникает исключение
                                # уже не было времени разбираться
            continue
    else:
        break
print('Введенный список значений: \n', ls)

b, lf, n = '', '', len(ls)
if len(ls) % 2 == 1:
    lf = ls[len(ls)-1]
for i, l in enumerate(ls):
    if i % 2 == 0:
        b = l
        ls.pop(i)
    else:
        ls.insert(i, b)
if n % 2 == 0:
    ls.append(b)
else:
    ls.append(lf)
print(ls)