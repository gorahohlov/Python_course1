#1 ----------------------------------

lst = [3.14, 0b01010, 1977, 'SDFFF', 2021, 0x4f3a, 2.71828, 'abcd']
print(lst)
print('#элемента|значение| тип элемента')
print('-'*34)
for a, i in enumerate(lst):
    print(f'{a:>8} |{i:>8}|{type(i)}')
print('-'*34)