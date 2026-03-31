from math import *
import re
from features import *

import math
a = 123456789
b = 223456789
arr = []

for i in range(int(a ** 0.25), int(b ** 0.25) + 1):
    show_percent(int(a ** 0.25), int(b ** 0.25) + 1, i, 10)
    for j in range(2, int(i ** 0.5) + 1):
        if not i % j:
            break
    else:
        if i > 1:
            arr.append([i ** 4, i ** 3])

for pair in arr:
    print(pair[0], pair[1])

for i in range(45, 1233947):
    show_percent(45, 1233947, i, step=10000)

print('good')

def def27858():
    dict = {}

    maxi = 0

    maxNumber = 0
    maxCount = 0
    for number in range(1201150, 1202010):
        count = 0
        num_sqrt = sqrt(number)
        for div in range(1, int(num_sqrt) + 1):
            if number % div == 0:
                count += 1
        count*= 2
        if num_sqrt == int(num_sqrt):
            count-=1
        
        dict.update({number:count})


    for key, value in dict.items():
        if value > maxCount:
            maxCount = value
            maxNumber = key    

    print(maxCount, maxNumber)
def task57432():
    pattern = re.compile(r'^12\d\d1\d*56$')
    for number1 in range(123405, 10**8 + 1):
        if number1 % 317 == 0 and pattern.fullmatch(str(number1)):
            print(number1, number1//317)

def task85701():
    
    for number in range(10**9 -1, 10**8 + 1, -1):
        count=0
        number_sqrt = sqrt(number)
        for div in range(1 , int(number_sqrt) + 1):
            if number % div == 0:
                count+=1 
        count*= 2

        if (number_sqrt == int(number_sqrt)):
            count-= 1


        if (number - count) % 23 == 0:
            print(number)


#task85701()
def task29673():
    for number in range(123456789,223456790):
        show_percent(123456789, 223456790, number, 10000000)
        maxdel = 1
        count = 0
        number_sqrt = sqrt(number)
        for div in range(2, int(number_sqrt) - 1):
            if number % div == 0:
                count+=1 
                if maxdel < div:
                    maxdel = div
                    
        count*= 2
        
        if (number_sqrt == int(number_sqrt)):
            count-= 1
        count-= 2

        if count == 3:
            print(number, maxdel*2)

task29673()