import numpy as np

n, k = map(int, input().split())
#c = [1000000000] * n
c = np.random.randint(9999990, 1000000000, n)
#print(c)
ans = 0
cnt = [0] * (n-k+1)

for i in range(n-k+1):
    cnt.append(len(set(c[i:i+k])))
print(max(cnt))
"""
for i in range(n-k+1):
    a = set(c[i:i+k])
    leng = len(a)
    if ans < leng:
        ans = leng
        if ans == k:
            break
print(ans)
"""