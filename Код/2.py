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
                        
# task18704()

def task84664():
    print('x w z y')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if ((w<=y) <= (z<=x) or (not(z))) == 1:
                        print(x, w, z, y)
# k84664()

def task76105():
    print('x w z y')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((x<= (not(y))) and (x or w)) <=(not(z))) == 0:
                        print(x, w, z, y)
# task76105()

def task69880():
    print('x w z y')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if (((x <= y)<=z)or (not(w))) == 0:
                        print(x, w, z, y)