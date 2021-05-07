# 1. -----------------------------------

a = ''
with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        a = input('Введите строку для сохраниеня в файле, Enter для завершения ввода: \n')
        if a == '':
            break
        f.write(a + '\n')
