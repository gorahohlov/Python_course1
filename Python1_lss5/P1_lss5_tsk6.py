# 6. -----------------------------------

dct = {}
with open('text3.txt', 'r', encoding='utf-8') as f_obj:
    for ln in f_obj:
        lst = ln.split()
        k = lst[0][:-1]
        smm = 0
        for n in lst:
            if n.find('(') == -1:
                continue
            else:
                smm += int(n[:n.find('(')])
        dct[k] = smm
print(dct)
