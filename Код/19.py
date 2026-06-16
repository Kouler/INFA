def task48440(k, x):
    if (x == 3 or x ==5) and k >= 103: return True
    if x == 5 and k < 103: return False
    if k >= 103: return False

    if k % 3 != 0:
        if x % 2 == 0:
            res = False
            if (k+1) % 3 != 0: res = res or task48440(k+1, x+1)
            if (k+2) % 3 != 0: res = res or task48440(k+2, x+1)
            if (k*2) % 3 != 0: res = res or task48440(k*2, x+1)
            return res 
        else:
            res = True
            if (k+1) % 3 != 0: res = res and task48440(k+1, x+1)
            if (k+2) % 3 != 0: res = res and task48440(k+2, x+1)
            if (k*2) % 3 != 0: res = res and task48440(k*2, x+1)
            return res
    
for k in range (1,102):
     if task48440(k, 1):
          print(k)