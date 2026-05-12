def task58225(num, end, was_forty):
    if num == 40: was_forty = True
    
    if num == end:
        if (was_forty):
            return 1
        else:
            return 0
    elif num < end or num == 20:
        return 0
    elif (not was_forty and num < 40):
        return 0
    else:
        return task58225(num - 2, end, was_forty) + task58225(num // 2, end, was_forty)
    
print(task58225(80, 1, False))