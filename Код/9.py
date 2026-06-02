f = open('./ods_files/9(1).csv')
sp = f.readlines()
count = 0
table = [[int(x)for x in st.split(';')] for st in sp]
for i in range(0, len(table)):
    if len(set(table[i])) != 6:
        interest = 0
        for j in range(0, 6):
            if table[i].count(table[i][j]) == 1:
                flag = False
                for Y in range(max(i-1, 0), min(len(table), i+2)):
                    for X in range(max(j-1, 0), min(6, j+2)):
                        if table[Y][X] < table[i][j]:
                            flag = True
                if flag:
                    interest += 1
        if interest >= 3:
            count += 1
print(count)