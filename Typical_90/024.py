n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
diff = 0
for i in range(n):
    diff += abs(a[i]-b[i]) 
if diff > k:
    print('No')
    exit()
if diff % 2 != k % 2:
    print('No')
    exit()

print('Yes')