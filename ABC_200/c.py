n = int(input())
a = [int(x) for x in input().split()]
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if (a[i]-a[j]) % 200 == 0:
            cnt += 1

print(cnt)