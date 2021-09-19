n = int(input())
a = [int(x) for x in input().split()]
cnt = 0

while True:
    for i, au in enumerate(a):
        if au % 2 == 1:
            break
        if i == n-1:
            for j, ai in enumerate(a):
                a[j] = ai / 2
            cnt += 1
    
    if i < n-1:
        print(cnt)
        break