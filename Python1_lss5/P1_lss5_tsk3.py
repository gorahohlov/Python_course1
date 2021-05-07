# 3. -----------------------------------

n, sal = 0, 0
with open('salary.txt', 'r', encoding='utf-8') as f_obj:
    print('Доска почета. Сотрудники с зарплатой меньше 20000 ₽: ')
    for ln in f_obj:
        if float(ln.split()[1]) < 20000:
            print(ln.split()[0])
        sal += float(ln.split()[1])
        n += 1
    print(f'Средняя зарплата по компании: {round(sal / n)} ₽')


# 3. /вариант 2/ -----------------------
n, sl = 0, 0
with open('salary.txt', 'r', encoding='utf-8') as f_obj:
    cntx = f_obj.readlines()
    for i in cntx:
        if float(i.split()[1]) < 20000:
            print(i.split()[0])
        sl += float(i.split()[1])
        n += 1
    print(f'средняя зарплата: {round(sl / n)}')
