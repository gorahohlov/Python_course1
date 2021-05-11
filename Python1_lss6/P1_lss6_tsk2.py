
# 2. -------------------------------------

class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w
        mssa = self._length * self._width * 25 * 5
        print(f'Масса асфальта для покрытия толщиной 5 см: {mssa}')

rd = road(100, 6)
