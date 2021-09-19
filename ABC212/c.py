n, k = map(int, input().split())
c = ([int(x) for x in input().split()])
d = []
ans = 0

for i in range(n):
    d.append(c[i])
    if i < k-1:
        continue
    a = set(d)
    leng = len(a)
    if ans < leng:
        ans = leng
        if ans == k:
            break
    d.pop(0)
print(ans)
