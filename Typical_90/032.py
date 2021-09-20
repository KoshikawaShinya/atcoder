from itertools import permutations

n = int(input())
c = False
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
kenaku = [[False for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    kenaku[x][y] = True
    kenaku[y][x] = True
ans = 10**(30)
for p in permutations(range(n), n):
    time = 0
    flag = True
    for i in range(n):
        if i < n-1 and kenaku[p[i]][p[i+1]]:
            flag = False
            break
        time += a[p[i]][i]
    if flag:
        c = True
        ans = min(ans, time)
if c:    
    print(ans)
else:
    print(-1)