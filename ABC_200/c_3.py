n = int(input())
a = [int(x) for x in input().split()]
cnt = [0] * 200
c = 0

for i in range(n):
    b = int(a[i] % 200)
    c += cnt[b]
    cnt[b] += 1

print(c)