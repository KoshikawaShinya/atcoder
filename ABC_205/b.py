n = int(input())
a = list(map(int, input().split()))
b = [x+1 for x in range(n)]
a.sort()
if a == b:
    print('Yes')
else:
    print('No')
