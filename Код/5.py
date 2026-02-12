def f(n):
    nb = str(bin(n)[2:])
    if (n%5==0):
        p = str(bin(5)[2:])
        nb+= p
    else:
        nb+= "1"
        ns = int(nb,2)
    if int(nb,2)%7==0:
        s = str(bin(7)[2:])
        r = nb + s
    else:
        r = nb+ "1"
    return int(r,2)
maxel = 0
ii = 0
for i in range(1000000,0, -1):
    if f(i) < 1728404: 
        maxel = f(i) 
        ii = i
        break
if f(i) < 1728404: 
    print (maxel, ii)

#ФУНКЦИЯ ПЕРЕВОДА В N-тую СИСТЕМУ СЧИСЛЕНИЯ
def bitch(n, BASE = 3):
    s = ""
    while n > 0:
        s+= str(n % BASE)
        n//= BASE
    
    return s[::-1]

def task81471(n):
    if (n % 3 == 0):
        return '1' + bitch(n) + '02'
    else:
        return bitch((n % 3) * 4) + bitch(n)

print('-------------')
#sto_tridtsat_pyat_blyat = 135
for i in range(0, 1000000):
    if int(task81471(i), 3) > 135:
        print(i)
        break
        
def get_result(a, b, c):
    left = a * b
    right = b * c

    return int(str(left) + str(right), 10) if left > right else int(str(right) + str(left), 10)

print('--------------')
def task13590():
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                if get_result(a, b, c) == 205:
                    print(a, b, c)
                    return


task13590()

print('--------------')

def get_res(a, b, c, d):
    ab = a + b
    cd = c + d
    return int(str(ab)+ str(cd), 10) if ab < cd else int(str(cd)+ str(ab), 10)

def task13563():
    count = 0
    for a in range (1,10,2):
        for b in range (1,10,2):
            for c in range (1,10,2):
                for d in range (1,10,2):
                    if get_res(a, b, c, d) == 616:
                        count+=1
    print(count)
                        
print(get_res(7,5,1,1))
task13563()                        

    
def task76673(n):
    s = str(bin(n)[2:])
    if s.count("1") < s.count("0"):
        index = s.find("0")
        s = s[:index] + '1' + s[index+1:]
    else:
        index = len(s) - (s[::-1]).find("1") - 1
        s = s[:index] + '0' + s[index+1:]
    
    
    return abs(n - int(s,2))

print(task76673(28))

max = 0
for i in range(1000000000, 1, -1):
    res = task76673(i)
    if i % 1000000 == 0: print("[", max, "]")
    if res > max:
        max = res
    elif max > res:
        break

print(max)