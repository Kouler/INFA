from math import*

def task28545():
    for i in range(1, 1000000):
        n = 2**i
        v = 320*240 * n
        if v < 80*1024*8:
            print(i)
            
task28545()
        