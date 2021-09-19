n = int(input())
a, b, c = [int(x) for x in input().split()]
l = 9999
num = 10000
for i in range(l):
    if a*i > n:
        break
    for j in range(l+1-i):
        if a*i + b*j > n:
            break

        if (n - (a*i + b*j)) % c == 0:
            k = (n - (a*i + b*j)) / c
            num = min(num, i+j+k)
print(int(num))

