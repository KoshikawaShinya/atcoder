import numpy as np
n, m = [int(x) for x in input().split()]
city = []
cnt = np.eye(n)
count = 0

for _ in range(m):
    city.append([int(x) for x in input().split()])

for i in range(m):
    cnt[city[i][0]-1][city[i][1]-1] += 1

cnt = np.array(cnt)

for _ in range(2):
    cnt += np.dot(cnt, cnt)

print(np.sum(cnt >= 1))