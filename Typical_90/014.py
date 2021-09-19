n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()
summ = 0
for i in range(n):
    summ += abs(a[i]-b[i])

print(summ)