for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
                if (not((not(x) or y) and not(w)) or not(z and not(y and w))) == 0:
                    print(x, y, w, z)

def task18704():
    for x in range(2):
        for y in range(2):
            for w in range(2):
                for z in range(2):
                    if ((x or (not(y))) and (not(w == z)) or w) == 1:
                        print(z, y, w, x)
                        
task18704()
#x y w z 
#0 0 0 1
#0 1 0 1
#1 1 0 1
#0 0 0 1
#0 0 1 0
#0 0 1 1
#0 1 1 0
#0 1 1 1
#1 0 0 1
#1 0 1 0
#1 0 1 1
#1 1 0 1
#1 1 1 0
#1 1 1 1