#5 ----------------------------------

m_list = [7, 5, 3, 3, 2]
m_list.reverse()
a = int(input('Введите натуральное число: \n'))
if a >= max(m_list):
    m_list.append(a)
elif a <= min(m_list):
    m_list.insert(0, a)
elif a <= max(m_list) and a >= min(m_list):
    for i, ml in enumerate(m_list):
        m1 = 0
        if a == ml:
            m_list.insert(i, a)
            break
        if a > ml:
            m1 = ml
        if a < ml and a > m1:
            m_list.insert(i, a)
            break
#else:
#    m_list.insert(m_list.index(a), a)
m_list.reverse()
print(m_list)