# 2.-----------------------------------

lst_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst_2 = []

# вариант 2.1
i1 = iter(lst_1)
i2 = iter(lst_1)
next(i2)

for elm in i2:
    if elm > next(i1):
        lst_2.append(elm)

print(lst_2)


# вариант 2.2
a = lst_1[0]

def chck_equal1(ar_1):
    global a
    if ar_1 > a:
        a = ar_1
        return ar_1
    else:
        a = ar_1
        return

lst_2 = [chck_equal1(i) for i in lst_1]

lst_2 = [elm for elm in lst_2 if elm]

print(lst_2)


# вариант 2.3
a = lst_1[0]

def chck_equal2(ar_1):
    global a
    if ar_1 > a:
        a = ar_1
        return True
    else:
        a = ar_1
        return False

lst_2 = [i for i in lst_1 if chck_equal2(i)]

print(lst_2)


# вариант 2.4
gnr = (i for i in lst_1)
a = lst_1[0]
lst_2 = []
for i in gnr:
    if i > a:
        lst_2.append(i)
    a = i

print(lst_2)
