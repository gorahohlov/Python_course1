# 3. -------------------------------

v_1 = float(input('Введите первое число: '))
v_2 = float(input('Введите второе число: '))
v_3 = float(input('Введите третье число: '))

def my_func(var_1, var_2, var_3):
    if var_1 >= var_2:
        sm = var_1
        if var_3 >= var_2:
            sm += var_3
        else:
            sm += var_2
    else:
        sm = var_2
        if var_1 >= var_3:
            sm += var_1
        else:
            sm += var_3
    return sm

print(my_func(v_1, v_2, v_3))
