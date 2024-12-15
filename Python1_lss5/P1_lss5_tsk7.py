# 7. -----------------------------------
import json

dct1, dct2, n, lst1, lst2, pftf, avg_prft = {}, {}, 0, [], [], 0, 0
with open('text3.txt', 'r', encoding='utf-8') as f_obj:
    for ln in f_obj:
        lst1 = ln.split()
        prft = float(lst1[2]) - float(lst1[3])
        dct1[lst1[0]] = prft
        avg_prft += (0, prft)[prft >= 0]
        n += (0, 1)[prft >= 0]
    dct2['average_profit'] = avg_prft / n
    lst2.append(dct1)
    lst2.append(dct2)
    print(lst2)

with open('jsn_file.json', 'w') as f_j:
    json.dump(lst2, f_j)
