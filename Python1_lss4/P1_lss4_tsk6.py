# 6.-----------------------------------

from itertools import count
lst_6 = []
for elm in count(3):
    if elm == 10:
        break
    else:
        lst_6.append(elm)
print(lst_6)

from itertools import cycle
lst_7, k = [], 0
for elm in cycle('python_'):
    if k > 27:
        break
    lst_7.append(elm)
    print(elm)
    k += 1
print(lst_7)
