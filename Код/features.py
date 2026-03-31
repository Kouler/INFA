from math import log
import sys
import time

def delete_last_line():
    """Deletes the last line in the STDOUT (works in most terminals)."""
    # Move cursor up one line
    sys.stdout.write('\x1b[1A') 
    # Clear the entire current line
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush() 

def show_percent(start, end, current_number, step=10):
    if (current_number % (abs((end - start) // step))) == 0:
        percent = ((current_number - start) // ((end - start) // step))
        
        if (percent > 0): delete_last_line()
        
        if (step <= 100):
            show = round(((current_number - start) / ((end - start) / step)) * 100 / step)
        else:
            digit = 0
            s = step
            while (s > 0):
                s//= 10
                digit+= 1
            
            show = round(((current_number - start) / ((end - start) / step)) * 100 / step, digit - 2)

        print(str(show) + '% [', end='')

        STATUS_BAR_LIMIT = 40
        if (step > STATUS_BAR_LIMIT):
            percent = percent * STATUS_BAR_LIMIT // step
            step = STATUS_BAR_LIMIT

        for x in range(0, percent):
            print('-', end='')
        for x in range(percent, step):
            print(' ', end='')
        
        print(']')
    

