n, k = [int(x) for x in input().split()]
mul = 0

for i in range(n):
    for j in range(k):
        mul += (i+1)*100 + (j+1)
    
print(mul)