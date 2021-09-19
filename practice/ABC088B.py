n = input()
a = [int(x) for x in input().split()]
alice = 0
bob = 0
flag = True

while True:
    num = 0
    index = 0
    for i, ab in enumerate(a):
        if(ab > num):
            num = ab
            index = i
    
    if flag == True:
        alice += num
        flag = False
    else:
        bob += num
        flag = True
    
    del a[index]

    if len(a) == 0:
        break

print(alice-bob)

    
    