def task48402():
    x = '0123456789'
    for digit in x:
        number = int('3' + digit + 'DA', 14) + int('5' + digit + 'A6', 12)
        if number % 81 == 0:
            answer = (number / 81)
            return (answer)

def task48397():
    x = '0123456789'
    for digit in x:
        number = int('8'+ digit + '71', 13) + int('3'+ digit + 'DF',17)
        if number % 197 == 0:
            return (number // 197)
# print(task48397())
#print(task48402())
            

def bitch(n, BASE):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ""
    while n > 0:
        s+= alphabet[n % BASE]
        n//= BASE
    return s[::-1]








#print(bitch(2030, 7))

def task71001():
    for x in range(2030,1,-1):
        number = (7**170 + 7**100 - x)
        n7 = bitch(number, 7)
        if n7.count('0') == 71:
            return x
            

#print(task71001())

def task48385():
    p=9
    numbers = '012354678'
    for x in numbers:
        for y in numbers:
            for z in numbers:
                for w in numbers:
                    if int(z + x + y + x + '4', p) + int(x + y + '658', p) == int(w + z + x + '73', p):
                        print(int(x + y + z + w, p))    
#task48385()  
 
def task76711():
    numbers = '0123546789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for p in range(12, 37):
        for x in numbers[1:p]:
            for y in numbers[:p]:
                for z in numbers[1:p]:
                    if int(z + x, p) + int(x + y, p) == int(z + y + 'B', p):
                        print(x+y+z+'_'+str(p)+':', int(x + y + z, p))    
#task76711()  

def task9367():
    a = str(bitch((9**8+3**5-9), 3))
    ac = a.count('2')
    print(ac)
#task9367()

def dosrok():
    count = 0
    s = bitch(2*2187**567 + 729**566 - 2 * 243**565 + 81**564 - 2*27**563 - 6561, 27)
    for char in s:
        if char in "ACEGIKMOQ":
            count += 1
    print(count)
#dosrok()    



def hp(n, b):
    a = ''
    alphavet = sorted('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    while n > 0:
        a += alphavet[n % b]
        n//=b
    return a[::-1]

def task40730():
    s = bitch(3*125**6+2*25**9+5**12-625, 5)
    count = s.count("0")
    print(count)
#task40730()

def task76711():
    alph = sorted("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for p in range(12, 37):
        for x in alph[1:p]:
            for y in alph[:p]:
                for z in alph[1:p]:   
                    if int(z + x, p) + int(x + y, p) == int(z+y+'B',p):
                        print(int(x + y +z, p))
#task76711()

def task16445():
     s = bitch(49**6 + 7**18 - 21, 7)
     count = s.count('6')
     print(count)
# task16445()

def task60292():
    x = bitch(3*3125**8+2*625**7-4*625**6+3*125**5-2*25**4-2024, 25)
    count = x.count("0")
    print(count)
task60292()