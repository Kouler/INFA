#from functools import *
import sys
sys.setrecursionlimit(1000000)
#@lru_cache(None)
def task59694(n):
    if n < 11:
        return n
    else:
        return n + task59694(n-1)    
task59694(1009)

print(task59694(2024)-task59694(2021))

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

print(task81482(43000))       

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
task51985()    

        