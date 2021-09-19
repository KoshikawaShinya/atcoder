import numpy as np

h, w, n = map(int, input().split())
card = []
a_ = []
b_ = []
for i in range(n):
    a, b = map(int, input().split())
    a_.append(a)
    b_.append(b)
    card.append([a, b])

a_i = np.array(sorted(a_))

for i, ama in enumerate(a_i):
    if i == 0:
        a_i[i:] -= abs(1 - ama)
    else:
        a_i[i:] -= abs(ama - )
print(a_i)