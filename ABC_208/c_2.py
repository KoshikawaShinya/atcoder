n = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a = sorted(a)
b = sorted(b)
c = 200000
index_a = 0
index_b = 0

for i in range(len(a)):
    for j in range(len(b)):
        tmp = abs(a[i] - b[j])
        if c > tmp:
            c = tmp
print(c)
