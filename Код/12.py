#s = '1' + '8' * 80
#while '18' in s or '288' in s or '3888' in s:
#    if '18' in s:
#        s = s.replace('18','2',1)
#    elif '288' in s:
#        s = s.replace('288','3',1)
#    else:
#        s = s.replace('3888', '1',1)
#print(s)
s = "1" * 78
while "111" in s:
        s = s.replace("111", "2", 1)
        s = s.replace("222", "11", 1)
print(s)

x = '2' + '3' *140
while '2' in x:
        if '23' in x:
                x = x.replace('23','3332',1)
        else:
                x = x.replace('2','333', 1)
print(int(x))

s = '333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333'
print(len(s)*3*3)