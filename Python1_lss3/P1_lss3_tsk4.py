# 4. -------------------------------

mntss = float(input('Введите действительное положительное число: '))
expnt = int(input('Введите целое отрицательнгое число: '))

def my_func_1(m, ex):
    # res = m ** ex
    return m ** ex

print(my_func_1(mntss, expnt))

def my_func_2(m, ex):
    # if ex == 0: # пардон// по условию задачи порядок степени должен быть отрицательным, 0 это неотрицательное число!
    #     res = 1
    # else:
    ex = abs(ex)
    for i in range(ex - 1):
        m *= m
    res = 1 / m
    return res
print(my_func_2(mntss, expnt))
