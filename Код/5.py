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

#print('-------------')
#sto_tridtsat_pyat_blyat = 135
# for i in range(0, 1000000):
#     if int(task81471(i), 3) > 135:
#         print(i)
#         break
        
# def get_result(a, b, c):
#     left = a * b
#     right = b * c

#     return int(str(left) + str(right), 10) if left > right else int(str(right) + str(left), 10)

# #print('--------------')
# def task13590():
#     for a in range(1, 10):
#         for b in range(0, 10):
#             for c in range(0, 10):
#                 if get_result(a, b, c) == 205:
#                     print(a, b, c)
#                     return


# #task13590()

# #print('--------------')

# def get_res(a, b, c, d):
#     ab = a + b
#     cd = c + d
#     return int(str(ab)+ str(cd), 10) if ab < cd else int(str(cd)+ str(ab), 10)

# def task13563():
#     count = 0
#     for a in range (1,10,2):
#         for b in range (1,10,2):
#             for c in range (1,10,2):
#                 for d in range (1,10,2):
#                     if get_res(a, b, c, d) == 616:
#                         count+=1
#     print(count)
                        
# #print(get_res(7,5,1,1))
# #task13563()                        

    
# def task76673(n):
#     s = str(bin(n)[2:])
#     if s.count("1") < s.count("0"):
#         index = s.find("0")
#         s = s[:index] + '1' + s[index+1:]
#     else:
#         index = len(s) - (s[::-1]).find("1") - 1
#         s = s[:index] + '0' + s[index+1:]
    
    
#     return abs(n - int(s,2))

# #print(task76673(28))

# max = 0
# for i in range(1000000000, 1, -1):
#     res = task76673(i)
#     if i % 1000000 == 0: print("[", max, "]")
#     if res > max:
#         max = res
#     elif max > res:
#         break

# #print(max)

# def dosrok(n):
#     s = bin(n)[2:]
    
#     if s.count('1') % 2 == 0:
#         s = '10' + s[2:] + '0'
#     else:
#         s= '11' + s[2:] + '1'
    
#     return int(s,2)

# v = 0
# for i in range(1000,0,-1):
#     if dosrok(i) > 480:
#         v = i

# print("Minimum:", v)

# def task18785(n):
#     s = bin(n)[2:]
#     if s[-1] == "0":
#         s = "1" + s + "0"
#     else:
#         s = "11" + s + "11"

#     return  int(s,2)
        

# k = 0  
# #for i in range(10000, 0, -1):  
# #    if task18785(i) > 52:
# #        k = i    
# #print(k)

# def task15974(n):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s = s + '10'
#     if n % 2 != 0:
#         s = s + '01'
#     return(int(s, 2))
# for i in range (0, 10000):
#     if task15974(i) < 102:
#         print(task15974(i))

# from  features import *

# def task56533(n):
#     s = bin(n)[2:]
#     digits_sum = 0
#     for digit in str(n):
#         digits_sum+= int(digit)
#     if digits_sum%2==0:
#         s = s + '0'
#     else:
#         s = s + '1'
#     return int(s,2)

# count = 0
# for i in range(1_000_000_000, 1, -1):
#     if  987_654_321<= task56533(i) <=2_123_456_789:
#         show_percent(2, 1_000_000_000, 1_000_000_000-i, 1000)
#         count+=1

# print(count)

def summ(n):
    sumi=0
    while n>0:
        sumi+=n%10
        n=n//10
    return sumi
o1 = 0
o2 = 0
q1 = bin(987654321)[2:]
q2 = int(q1[:len(q1) - 3], 2)
 
for n in range(q2 - 100, q2 + 100):
    s = bin(n)[2:]
    for i in range(3):
        if summ(int(s,2))%2==0:
            s += '0'
        else:
            s += '1'
    r = int(s, 2)
    if 987654321 <= r and r <= 2123456789:
        o1 = n
        break
k1 = bin(2123456789)[2:]
k2 = int(k1[:len(k1) - 3],2)
for n in range(k2 - 100, k2 + 100):
    s = bin(n)[2:]
    for i in range(3):
        if summ(int(s, 2)) % 2 == 0:
            s += '0'
        else:
            s += '1'
    r = int(s, 2)
    if 987654321 <= r and r <= 2123456789:
        o2 = n
# print(o2 - o1 + 1)
 
def task76673(n):
    s = bin(n)[2:]
    if s.count('0') > s.count('1'):
        i = s.find('0')
        if i >= 0:
            s = s [:i] + '1' + s[i+1:]
    else:
        i = s.rfind('1')
        if i >= 0:
            s = s [:i] + '0' + s[i+1:]
    r = int(s, 2)
    return(abs(n-r))
max_r=0
min_n=0
for num in range(0, 10**9 +1):
    if max_r < task76673(num):
        max_r = task76673(num)
        min_n = num
    if num % 10000000 == 0:
        print(min_n)

    
