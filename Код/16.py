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
