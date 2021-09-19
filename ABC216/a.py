n, m = map(int, input().split())
a = []
cnt = [0] * m
for i in range(m):
    k = input()
    a.append([int(x) for x in input().split()])
    cnt[a[i][0]-1] += 1

for i in range(n):
    if 2 in cnt:
        
    else:
        print('No')
        exit()
print('Yes')