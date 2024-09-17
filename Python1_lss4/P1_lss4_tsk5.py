# 5.-----------------------------------

print([i for i in range(100, 1001) if i % 2 == 0])

from functools import reduce

print(reduce((lambda a1, a2: a1 * a2), [i for i in range(100, 1001) if i % 2 == 0]))
