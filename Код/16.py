#from functools import *
import sys
sys.setrecursionlimit(1000000)
#@lru_cache(None)
def task59694(n):
    if n < 11:
        return n
    else:
        return n + task59694(n-1)    
#task59694(1009)

#print(task59694(2024)-task59694(2021))

def task81482(n):
    if n <= 7:
        return n
    else:
        return g(n-3)*3
def g(n):
    if n<=7:
        return n 
    else:
        return g(n-1)+4

#print(task81482(43000))       

def F(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + F(n//10)
        

def task51985():
    percent = (1134567010 - 237567892) // 100
    out = 0
    k=0
    for n in range(237567892, 1134567010):
        if (n % percent == 0) :
            print(str(out)+ '%')
            out += 1
        if F(n) > F(n+1):
            k+=1
    print(k)
#task51985()    

def task36871():
    k=0
    for n in range (0,1001):
        if f36871(n) == 3:
            k+=1
    print(k)


def f36871(n):
    if n == 0:
        return 0
    if n > 0 and n%2==0:
        return f36871(n/2)
    if n%2!=0:
        return 1+f36871(n-1)
#task36871()

def task6189(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return (task6189(n-2)*n)
#print(task6189(7))

def task35474(n):
    if n == 0:
        return 0
    if (n > 0) and (n % 3 == 0):
        return task35474(n//3)
    if (n % 3 > 0):
        return ((n % 3) + task35474(n - (n % 3)))
     
#for i in range(1000):
#        if task35474(i) == 11:
#            print(i)
#            break

def taskg(n):
    if n == 1:
        return 1
    if n>=2:
        return taskf(n-1)+taskg(n-1)
def taskf(n):
    if n == 1:
        return 1
    if n>=2:
        return taskf(n-1)-taskg(n-1)
    
# print(taskf(5)//taskg(5))

def task55812(n):
    if n >=2025:
        return n
    if n < 2025:
        return(n+3) + task55812(n+3)
# print(task55812(23)-task55812(21))

def task58226(n):
    if n == 1: return 1
    if n == 2: return 2
    if n > 2 and n % 2 == 0:
        return ((3*n+task58226(n-3))//3)
    if n > 2 and n % 2 != 0:
        return ((7*n+task58226(n-1)-task58226(n-2))//5)
print(task58226(35))
    