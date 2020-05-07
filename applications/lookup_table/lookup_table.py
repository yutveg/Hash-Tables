import math
import random

cache = {}

def build_lookup():
    for i in range(50000):
        x = random.randrange(2, 14)
        y = random.randrange(3, 6)
        slowfun(x, y)


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    if (x, y) not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[x, y] = v
        

    return cache[x, y]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
