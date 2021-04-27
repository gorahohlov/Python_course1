# 5. -------------------------------

s_1, f_1 = 0, True
def smma (lst_1):
    flg_1 = True
    s_1 = 0
    for i in lst_1:
        if i != 'q':
            s_1 += float(i)
        else:
            flg_1 = False
            break
    return s_1, flg_1

while f_1:
    lst_1 = input('Введите строку чисел разделенных пробелом:\n(для завершения ввода нажмите Enter;)\n(для окончания нажмите символ q;)\n').split()
    s_1 += smma(lst_1)[0]
    f_1 = smma(lst_1)[1]
    print(s_1)
