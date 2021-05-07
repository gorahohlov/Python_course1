# 5. -----------------------------------

s = 0
with open('text3.txt', 'w+', encoding='utf-8') as f_obj:
    f_obj.write(input('Введите строку чисел разделенных пробелом: '))
    f_obj.seek(0)
    for elm in f_obj.readline().split():
        s += float(elm)
    print(s)
