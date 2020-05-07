"""
exps(x, y, z) =
     if x <= 0: y + z
     if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)
"""
cache = {}
def expensive_seq(x, y, z):
    # Implement me
    for i in range(10):
        if x <= 0:
           cache[x, y, z] = y + z
        if x > 0:
            cache[x, y, z] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        
        return cache[x, y, z]
        

print(expensive_seq(150, 400, 800))

