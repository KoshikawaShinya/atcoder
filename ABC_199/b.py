n = int(input())

a = [int(x) for x in input().split()]
ans = 0

for i in range(n):
    if a[i] > 10:
        ans += a[i] - 10

print(ans)

