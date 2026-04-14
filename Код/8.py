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


def dosrok():
    s = 'АПРЕЛЬ'
    last_count = 0
    ss = ''
    count = 0
    for i in product(sorted(s), repeat=5):
        count += 1
        if (i[0]!='Ь') and (i[0]!='Р') and i.count('Л') >=2 and count%2==0:
            print(i)
            last_count = count
            ss = i
    
    print("Last one:", last_count, "s:", ss)
dosrok()