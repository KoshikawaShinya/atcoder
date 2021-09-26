from collections import deque

n, q = map(int, input().split())
a = deque([x for x in input().split()])
for i in range(q):
    t, x, y = map(int, input().split())

    if t == 1:
        tmp = a[x-1]
        a[x-1] = a[y-1]
        a[y-1] = tmp
    elif t == 2:
        tmp = a.pop()
        a.appendleft(tmp)
    else:
        print(a[x-1])
