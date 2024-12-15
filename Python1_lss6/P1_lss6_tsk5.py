
# 5. -------------------------------------

class Stationary:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):

    def draw(self):
        print('Запуск отрисовки: ручка')

class Pencil(Stationary):

    def draw(self):
        print('Запуск отрисовки: карандаш')

class Handle(Stationary):

    def draw(self):
        print('Запуск отрисовки: маркер')

print('')
p = Pen('синяя ручка')
print(p.name)
p.draw()
print('')
pc = Pencil('красный карандаш')
print(pc.name)
pc.draw()
print('')
hn = Handle('зеленый маркер')
print(hn.name)
hn.draw()
