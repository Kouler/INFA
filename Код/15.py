def task57422():
    f = 0 
    
    for A in range(0, 1000):
        k = 0
        for x in range (0,100):
            for y in range (0,100):
                  f = (x>=12) or (3*x<y) or (x*y< A)
                  if f == 1:
                    k += 1
        if k == 10000:
            print(A)
            break
print(task57422())                    


def task48426():
    for A in range (1, 1000):
        k = 0
        for x in range (1, 1000):
            if ((72 % x == 0) <= ((120 % x != 0))) or (A-x>100):
                k+=1
        if k == 999:
            print(A)
            break
            
    
task48426()             

def task43509():
    for A in range(0, 10000):
         k = 0 
         for x in range(1, 1000):
            if (((x&28 != 0) or (x&45!=0)) <= ((x&17 == 0) <= (x&A != 0))):
                k+=1
         if k == 999:
            print(A)
            break
task43509()       







