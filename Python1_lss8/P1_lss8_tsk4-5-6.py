
# 4 Склад оргтехники. Задание #1

class OrgTechnic():
    u_volts = 220
    is_certified = True
    def __repr__(self):
        return f'{self.brand}_{self.model}_{self.__hash__()}'

class Printer(OrgTechnic):
    def __init__(self, brn, mdl, clr=True, cp=12):
        self.model = mdl
        self.brand = brn
        self.ink_colour = clr
        self.copies_per_min = cp
    def prnt(self, n, clr_mod=False):
        if clr_mod is False:
            t = f'Напечатано: {n} чернобелых копий'
        else:
            if self.ink_colour is True:
                t = f'Напечатано: {n} цветных копий'
            else:
                t = f'Принтер: {self.model} {self.brand} не поддерживает цветную печать!'
                self.stop_prnt()
        return t
    def stop_prnt(self):
        print(f'Печать принудительно остановлена!')


class Scaner(OrgTechnic):
    def __init__(self, brn, mdl, wght, frmt='A4', scns=6):
        self.brand = brn                # марка
        self.model = mdl                # модель
        self.format = frmt              # формат источника, по умолчанию A4
        self.scans_per_min = scns       # скорость сканирования
        self.weight = wght              # вес сканера
    def __str__(self):
        return f'Сканер: марка - {self.brand}, '\
               f'модель - {self.model}, '\
               f'формат - {self.format}, '\
               f'cкорость сканирования - {self.scans_per_min}, '\
               f'вес сканера - {self.weight}.'

class Copier(OrgTechnic):
    def __init__(self, brn, mdl, wght, cps=4, clr=True, frmt='A4'):
        self.brand = brn
        self.model = mdl
        self.weight = wght
        self.colour_mode = clr          # цветные копии Да/Нет
        self.format = frmt              # max формат бумаги исходника
        self.copies_per_min = cps
    def __str__(self):
        return f'Копир: марка - {self.brand}, '\
               f'модель - {self.model}, '\
               f'формат - {self.format}, '\
               f'скорость сканирования - {self.copies_per_min}, '\
               f'вес сканера - {self.weight}'

if __name__ == '__main__':
    p = Printer('HP', 'deskjet', clr=False)
    print(p)
    # p.ink_colour = False
    # print(p.prnt(6, clr_mod=True))
    s = Scaner('Epson', 'perfection', 1.5, frmt='A4')
    print(s)
    c = Copier('Canon', 'imagerunner', 8, clr=False, cps=20)
    print(c)


# 5 Склад оргтехники. Задание #2 Прием и передача.

class Store():
    def __init__(self):
        self.reg = {}                   # регистр остатов по каждому объекту хранилища реализован как словарь.
    def take_method(self, obj, qty):    # предметом учета я сделал сам объект ТМЦ, а не его атрибут
       self.reg[obj] = qty
    def give_method(self, other, obj, qty):
        if self.reg[obj] < qty:
            print('Передача товара не может быть выполнена. На складе недостаточно товара.')
            return
        else:
            self.reg[obj] -= qty
            if obj in other.reg:
                other.reg[obj] += qty
            else:
                other.reg[obj] = qty

# 6. Продолжаем работу на вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.

class IsNumb(Exception):
    @staticmethod
    def raiser_2(param_1):
        try:
            param_1.isdigit()
            return int(param_1)
        except ValueError:
            return False


class Depart(Store):
    def give_valid(self, other, obj):   # переопределяем метод Store.give_method() добавляя дополнительную функциональность.
        while True:
            print(f'Доступно для отгрузки: {other.reg[obj]}')
            q = input(f'Введите количество товара для отгрузки в департамент {self}: ')
            zeta = IsNumb.raiser_2(q)
            if zeta is False:
                print('Введено не число. Требуется ввести число! Давайте еще раз.')
                continue
            break
        Store.give_method(other, self, obj, zeta)


if __name__ == '__main__':
    st = Store()                        # создаём объект-экземпляр склада
    log_d = Depart()                    # создаём департамент логистики
    buh_d = Depart()                    # создаём департамент бухгалтерии
    st.take_method(c, 6)                # поступление на склад
    print('Склад:    ', st.reg)
    st.give_method(log_d, c, 4)         # отгрузка в департамент
    print('Склад:    ', st.reg)
    # print(hash(c))
    print('Лог_депт: ', log_d.reg)
    print('Бух_депт: ', buh_d.reg)
    st.give_method(buh_d, c, 1)
    log_d.give_method(buh_d, c, 2)
    st.take_method(p, 8)                # Приёмка от поставщика на склад p (принтеров)
    st.take_method(s, 12)               # Приёмка от поставщика на склад s (сканеров)
    st.give_method(log_d, p, 4)         # откуда: st, куда: log_d, какой ТМЦ: p (принтер)
    st.give_method(buh_d, p, 2)         # откуда: st, куда: buh_d, какой ТМЦ: p (принтер)
    st.give_method(log_d, s, 1)         # откуда: st, куда: log_d, какой ТМЦ: s (сканер)
    st.give_method(buh_d, s, 2)         # откуда: st, куда: buh_d, какой ТМЦ: s (сканер)
    print('Склад:    ', st.reg)
    print('Лог_депт: ', log_d.reg)
    print('Бух_депт: ', buh_d.reg)
    log_d.give_valid(st, p)             # откуда: st, куда: log_d, какой ТМЦ: p (принтер)
    print('Склад:    ', st.reg)
    print('Лог_депт: ', log_d.reg)
    log_d.give_valid(buh_d, c)          # откуда: buh_d, куда: log_d, какой ТМЦ: c (копир)
    print('Лог_депт: ', log_d.reg)
    print('Бух_депт: ', buh_d.reg)
