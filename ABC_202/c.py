n = int(input())
a = []
cnt = [0] * (n+1)
ans = 0

for _ in range(3):
    a.append([int(x) for x in input().split()])

for i in range(n):
    cnt[a[1][a[2][i]-1]] += 1

for i in range(n):
    ans += cnt[a[0][i]]

print(ans)
