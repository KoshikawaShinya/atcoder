import numpy as np

h, w = [int(x) for x in input().split()]
a = []

for _ in range(h):
    a.append([int(x) for x in input().split()])

a = np.array(a)

row_sum = np.tile(np.sum(a, axis=0), (h, 1))
col_sum = np.tile(np.sum(a, axis=1), (w, 1))

b = row_sum + col_sum.T - a
b = b.tolist()

for i in range(h):
    print(" ".join(map(str, b[i])))
