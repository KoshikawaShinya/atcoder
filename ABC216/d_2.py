n, k = map(int, input().split())
a = [int(x) for x in input().split()]

ma = max(a)
result = ma * k - k-1*(k)//2
print(result)
"""
sa = ma - k
sa_count = 0
for i in range(n):
    if a[i] >= sa:
        sa_count += 1
print(sa_count)
"""
