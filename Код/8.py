import itertools
from itertools import product

### № 76705
def task76705():
    otv = []
    for i in range(2,14):
        combs = [''.join(pair) for pair in itertools.combinations('123456789ABC', i)]
        otv.append(len(combs))
    print(sum(otv))


### № 27539
def task27539():
    COUNT = 0
    letters = ['B', 'O', 'R', 'I', 'S']
    for i1 in letters:
        print("1/6 good")
        for i2 in letters:
            for i3 in letters:
                for i4 in letters:
                    for i5 in letters:
                        for i6 in letters:
                            s = (i1+i2+i3+i4+i5+i6)
                            if s.count('B') == 1 and s.count('R') == 1 and s.count('S') <=1:
                                COUNT += 1 

    print(COUNT)

def task19059():

    saf = 'ИКНОТ'
    count = 0
    for i in product(saf, repeat =4):
        count+= 1
        if i[0] == 'О':
            print(count)
            return
        
    print("doesn't exist")



