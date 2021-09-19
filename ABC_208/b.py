x = input()
tmp = 10
flag = 1
b = set(x)
if len(b) == 1:
    flag = 0
else:
    for i, a in enumerate(x):
        a = int(a)
        if i > 0:
            if (a-1) == tmp or (a+9) == tmp:
                if i == 3:
                    flag = 0
            else:
                break

        tmp = a    

if flag == 0:
    print('Weak')
else:
    print('Strong')