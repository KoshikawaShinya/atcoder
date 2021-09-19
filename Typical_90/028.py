n = int(input())
a = []
l = 1001
ans = [0] * (n+1)
for i in range(l):
    a.append([0]*l)

for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    a[lx][ly] += 1
    a[rx][ry] += 1
    a[lx][ry] -= 1
    a[rx][ly] -= 1

for x in range(l):
    for y in range(1, l):
        a[x][y] += a[x][y-1]
for x in range(1, l):
    for y in range(l):
        a[x][y] += a[x-1][y]

for x in range(l):
    for y in range(l):
        if a[x][y] != 0:
            ans[a[x][y]] += 1

for x in ans[1:]:
    print(x)
        