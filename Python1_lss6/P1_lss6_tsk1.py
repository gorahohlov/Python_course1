
# 1. -------------------------------------
import time

class TrafficLight:
    __color = ''

    def running(self):
        while True:
            self.__color = 'red'
            print(f'Загорелся красный: {self.__color}')
            time.sleep(2)
            self.__color = 'yellow'
            print(f'Горит желтый. Приготовиться: {self.__color}')
            time.sleep(2)
            self.__color = 'green'
            print(f'Горит зеленый: {self.__color}')
            time.sleep(2)
            a = input('Нажмите q для выхода')
            if a == 'q':
                break

tl = TrafficLight()
tl.running()
# я не понял последний абзац задания - что мне нужно сделать в конкретно моем варианте кода,\
# в моем коде порядок будет один и тот же каждый раз.
