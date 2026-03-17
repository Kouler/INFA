from turtle import *
from math import sqrt
def tur():
    tracer(0)
    k=10
    lt(90)
    down()
    for i in range (2):
        fd(8*k); rt(150);fd(8*k); rt(30);

    up()

    for x in range(-50,50):
        for y in range(-50,50):
            goto(x*k,y*k)
            dot(3)

    input()
def tert():
    tracer (0)
    k=10
    ddd = 20 * sqrt(3)
    down()
    lt(90)
    rt(60)
    for i in range (2):
        fd(10*k);rt(120); fd(5*k); rt(240)
    rt(120)
    fd(3*k)
    rt(90)
    fd(ddd*k)
    rt(90)
    fd(8*k)
    rt(120)
    for i in range (2):
        fd(10*k);lt(120); fd(5*k); lt(240)

    for x in range(-50, 50):
        for y in range(-50, 50):
            goto(x*k,y*k)
            dot(3)
    input()
    
        
def ter():
    tracer(0)
    k=10
    lt(90)

    down()
    for i in range(7):
        fd(17*k); rt(90); fd(26*k); rt(90)
    up()
    fd(4*k)
    rt(90)
    fd(6*k)
    lt(90)
    down()
    for i in range(7):
        fd(278*k); rt(90); fd(345*k); rt(90)
    up()
    for x in range(-50, 50):
       for y in range(-50, 50):

            goto(x*k,y*k)
            dot(3)
    input()
ter()
   
    