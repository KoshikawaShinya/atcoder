import numpy as np

n, q = map(int, input().split())
a = np.array(list(map(int, input().split())))
k = []
for _ in range(q):
    k.append(int(input()))
k = np.array(k)

seisu = np.array([x+1 for x in range(max(k)+n)])
seisu = list(np.delete(seisu, [a-1])[k-1])
for i in seisu:
    print(i)