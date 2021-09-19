from itertools import permutations

n = int(input())
Max = 10**10
a = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
e = [set() for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    e[x].add(y)
    e[y].add(x)
ans = Max
for p in permutations(range(n)):
    