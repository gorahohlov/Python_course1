# 4. -----------------------------------

s, lst_1 = '', ['Раз', 'Два', 'Три', 'Четыре']
with open('text2.txt', 'r', encoding='utf-8') as f_obj1:
    for n, ln in enumerate(f_obj1):
        s += lst_1[n] + ' — ' + ln.split(' — ')[1]

with open('text3.txt', 'w', encoding='utf-8') as f_obj2:
    f_obj2.write(s)
