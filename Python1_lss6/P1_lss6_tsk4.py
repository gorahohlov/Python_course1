
# 4. -------------------------------------

class Car:

    def __init__(self, color, name, is_police, speed=60):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Машина начала движение.')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        # self.direction = direction
        # print(f'Машина повернула {self.direction}')
        print(f'Машина повернула {direction}')

    def show_speed(self, speed):
        print(f'Текущая скорость автомобиля: {speed}')


class TownCar(Car):

    def show_speed(self, speed):
        print(f'Текущая скорость автомобиля: {speed}')
        self.speed = speed
        if self.speed > 60:
            print(f'Максимальная разрешенная скорость 60. Превышение скорости!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self, speed):
        print(f'Текущая скорость автомобиля: {speed}.')
        self.speed = speed
        if self.speed > 40:
            print(f'Максимальная разрешенная скорость 40. Превышение скорости')

class PoliceCar(Car):
    pass

print('')
t = TownCar('white', 'Citroen', False)
print(t.name, t.color)
t.show_speed(60)
t.turn('направо')
t.show_speed(80)
print(f'Цвет автомобиля: {t.color}')
print(t.name, f'Полицейский автомобиль: {t.is_police}')
print('')
w = WorkCar('Black', 'Ford', False)
print(w.name, w.color)
w.turn('налево')
w.show_speed(70)
w.show_speed(35)
