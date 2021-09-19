n, a, b = [x for x in input().split()]
goke = 0

for i in range(int(n) + 1):
    st = list(str(i))
    at = [int(x) for x in st]
    mul = sum(at)

    if mul >= int(a) and mul <=int(b):
        goke += i

print(goke)
    
