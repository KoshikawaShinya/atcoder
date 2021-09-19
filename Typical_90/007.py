import bisect

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
q = int(input())
for i in range(q):
    b = int(input())
    index = bisect.bisect_left(a, b)
    if index >= len(a):
        index -= 1
    index_left = max([0, index-1])
    c = min([abs(a[index]-b), abs(a[index_left]-b)])
    print(c)
