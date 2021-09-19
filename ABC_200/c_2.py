import numpy as np

n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
a = np.array(a)
b = a

for i in range(n):
    b = b[1:]
    a = a[:-1]
    result = (a - b) % 200
    if np.any(result==0):
        cnt += np.count_nonzero(result == 0)

print(cnt)