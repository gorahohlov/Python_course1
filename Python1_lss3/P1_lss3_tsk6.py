# 6. -------------------------------

def int_func(txt_1):
    return txt_1.capitalize()

tx_1 = input('Введите латиницей строку из слов разделенных пробелом в нижнем регистре: \n')
lst_2 = []
for i in tx_1.split():
    lst_2.append(int_func(i))
print(' '.join(lst_2))
print(tx_1.title())
