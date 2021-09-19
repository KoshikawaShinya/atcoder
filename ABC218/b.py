S = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
b = []
for x in zip(*S[::-1]):
    a.append(x)
    print(*x,sep='')
for x in zip(*a[::-1]):
    b.append(x)
    print(*x,sep='')
print(a)
print(b)