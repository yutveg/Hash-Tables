
cache = {}
def expensive_seq(x, y, z):
    # Implement me
    for i in range(10):
        if x < 0:
           cache[x, y, z] = y + z
           
        if (x, y, z) not in cache:
            x = expensive_seq(i*2, i*3, i*4)
            cache[x, y, z] = x
    
        return cache[x, y, z]
        

print(expensive_seq(150, 400, 800))

