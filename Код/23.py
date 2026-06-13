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
    
#print(task58225(80, 1, False))

def task18724(st, en):
    if st > en:
        return 0
    if st == en:
        return 1
    if st < en:
        return(task18724(st+1,en)+task18724(st*3,en)+task18724(st+2,en))
# print(task18724(1,10)*task18724(10,12)*task18724(12,15))

def task5064(str, end):
    if str > end:
        return 0
    if str == end:
        return 1
    if str < end:
        return(task5064(str +1, end) + task5064(str *2, end) + task5064(str *3, end))
print(task5064(1,13))