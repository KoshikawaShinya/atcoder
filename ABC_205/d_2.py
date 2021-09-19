n, q = map(int, input().split())
a = list(map(int, input().split()))
j = 0
k = []
for _ in range(q):
    cnt = 0
    k.append(int(input()))
l = sorted(k)

for i in l:
    for j in range(j, n):
        if i >= a[j]-cnt:
            cnt += 1
        else:
            print(i+cnt)
            break
    if j == len(a)-1:
        print(i+cnt)


