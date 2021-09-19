n = int(input())
a = [int(x)-1 for x in input().split()]
b = [int(x)-1 for x in input().split()]
c = [int(x)-1 for x in input().split()]
count = 0

temp = [0] * (n+1)

for i in range(n):
    temp[b[c[i]]] += 1

for i in a:
    count += temp[i]

print(count)