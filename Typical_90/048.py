n, k = map(int, input().split())
ten = []
for i in range(n):
    a, b = map(int, input().split())
    a -= b
    ten.append(a)
    ten.append(b)
ten.sort(reverse=True)
ans = 0
for i in range(k):
    ans += ten[i]
print(ans)

