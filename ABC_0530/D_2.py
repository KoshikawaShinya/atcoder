import numpy as np

n, k = [int(x) for x in input().split()]
a = []
i_d = 0
j_d = 0
center = k**2 // 2
for _ in range(n):
    a.add([int(x) for x in input().split()])

a = np.array(a)
col = np.zeros_like(a)

for i in range(k):
    i_max = i + k
    for j in range(k):
        j_max = j + k

        col[i, j] = a[i:i_max, x:x_max]

print(col)
                




3 2
1 7 0
5 8 11
10 4 2