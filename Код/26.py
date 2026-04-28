def task46984():
    f = open('./txt_files/26_46984.txt')
    n = int(f.readline())
    a = [[0] * 10001 for j in range(10001)]
    for i in range(n):
        x, y = map(int, f.readline().split())
        a[x][y] = 1
    maxi = 0
    mini = 0
    for i in range(10001):
        count = 0
        m = 0
        for j in range(10001):
            if a[i][j] == 1:
                count += 1
                m = max(count, m)
            else:
                count = 0
        if m > maxi:
            maxi = max(maxi, m)
            mini = i
    print(maxi, mini)


def task78051():
    f=open('./txt_files/26_78051.txt')
    f.readline()
    times=[0]*1440
    for s in f:
        t1,t2=map(int, s.split())
        for t in range(t1,t2+1): times[t]+=1
    dlit=[1]
    smena=[]
    for i in range(1,len(times)):
        if times[i-1]==times[i]: dlit[-1]+=1
        else:
            dlit.append(1)
            smena.append(i)
    print(smena[-2],max(dlit))

task78051()

