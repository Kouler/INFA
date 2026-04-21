def task37336():
    s = [int(i) for i in open('./txt_files/17_1.txt')]
    max = -100001
    pair_count = 0
    for i in range(0, len(s) -1):
        if s[i] % 3 == 0 or s[i+1] % 3 == 0:
            pair_count+= 1
            if s[i] + s[i+1] > max:
                max = s[i] + s[i+1]
    print(pair_count, max)
#task37336()


def task59810():
    s = [int(i) for i in open('./txt_files/17_2.txt')]
    max = -10001
    pc = 0

    min = 10001
    for i in range (0, len(s)):
        if max < s[i] and s[i] % 100 == 24:
            max = s[i]
            
    for i in range(0, len(s) -2):    
        three_digit_count = 0
        three_sum = 0
        for j in range(0, 3):
            three_sum+= s[i+j]
            if len(str(s[i + j])) == 3:
                three_digit_count+= 1
                
        if three_digit_count == 1 and three_sum > max:
            pc+= 1
            if three_sum < min:
                min = three_sum

    print(pc, min)

#task59810()

def task61397():
    s = [int(i) for i in open('./txt_files/17_3.txt')]
    max = 0
    pc = 0
    for i in range(0, len(s)):
        if max < s[i] and s[i] % 100 == 17:
            max = s[i]

    max_sum = 0

    for i in range(0, len(s) -2):

        four_digit_count = 0 
        four_sum = 0
        del_pyt = 0

        for j in range(0, 3):
            four_sum += s[i + j] 
            if len(str(s[i + j])) == 4:
                four_digit_count+= 1
            if s[i + j] % 5 == 0:
                del_pyt+= 1

        
        if four_digit_count == 2 and del_pyt >= 1 and four_sum > max:
            pc+= 1
            if max_sum < four_sum:
                max_sum = four_sum
    print(pc, max_sum)    
#task61397()

def task76714():
    s = [int(i) for i in open('./txt_files/17_4.txt')]
    max = -1
    min = 10000000000
    pc = 0
    for i in range (0, len(s)):
        if max < s[i]:
            max = s[i]
        if min > s[i]:    
            min = s[i]



    max_sum = 0
    for i in range(0, len(s) - 2):
        five_count = 0
        #in_mas = 0
        #not_in_mas = 0
        
        contain_with_min = False
        doesnt_contain_with_max = True
        three_sum = 0
        for j in range(0, 3):
            three_sum+= s[i + j]
            if len(str(s[i + j])) == 5:
                five_count += 1
            if s[i + j] % 10 == min % 10:
                contain_with_min = True
            if s[i + j] % 10 == max % 10:
                doesnt_contain_with_max = False
                break

        if contain_with_min and doesnt_contain_with_max and five_count <= 1:
            pc+= 1
            if max_sum < three_sum:
                max_sum = three_sum
    print (pc, max_sum)

#task76714()

def task47221():
    s = [el.strip() for el in open('./txt_files/17_5.txt')]

    max3 = -10001
    for num in s:
        if num[-1] == '3' and int(num) > max3: max3 = int(num)

    pc = 0
    max_sum = 0

    for i in range(0, len(s) -1):
        if (
            (s[i][-1] == '3') ^ (s[i+1][-1] == '3')
        ) and (
            (int(s[i])**2 + int(s[i+1])**2) >= (max3**2)
        ):
            pc+=1
            if max_sum < int(s[i])**2 + int(s[i+1])**2:
                max_sum = int(s[i])**2 + int(s[i+1])**2

    print(pc, max_sum)
#task47221()

def task59842():
    s = [int(i) for i in open('./txt_files/1777_59842.txt')]

    pc = 0
    max = -1000001
    for num in s:
        if str(num)[-2:] == '29' and max < num:
            print(num)
            max = num

    sum_three = 0 
    max_sum = 0

    print(max)

    for i in range (0, len(s) - 2):
        five_count = 0
        sum_three = sum(s[i:i+3])
        
        for shift in range(0, 3):
            if abs(s[i + shift]) > 9999 and abs(s[i + shift]) < 100_000:
                five_count+= 1

        if (five_count == 2 and sum_three <= max):
                pc+=1
                if max_sum < sum_three:
                    max_sum = sum_three
    print(pc, max_sum)

task59842()

