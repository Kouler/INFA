from math import *
import re
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


task85701()
