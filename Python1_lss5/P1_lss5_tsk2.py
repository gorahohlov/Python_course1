# 2. -----------------------------------

n = 0
with open('text.txt', 'r', encoding='utf-8') as f_obj:
    print('|' + ('-' * 28) + '|')
    print('|#строки| кво_слов1|кво_слов2|')
    print('|' + ('-' * 28) + '|')
    for ln in f_obj:
        n += 1
        qty_w1 = len(ln.split())
        qty_w2 = ln.count(' ') + 1  # или так
        print(f'|{n:>7}| {qty_w1:>9}| {qty_w2:>8}|')
        print('|' + ('-' * 28) + '|')
    print(f'|Всего в файле: {n} строк      |')
    print('|' + ('-' * 28) + '|')
