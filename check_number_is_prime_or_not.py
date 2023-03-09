# check prime number


num = 11
if num == 1 or num == 2 or num == 0:
    print('prime')
else:
    flag = False
    for i in range(2,(num//2)+1):
        if (num%i) == 0:
            flag = False
            break
    else:
        flag = True
    if flag:
        print("prime")
    else:
        print("not prime")
        
       
