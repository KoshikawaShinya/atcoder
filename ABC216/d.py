import heapq
q = int(input())
a = []
offset = 0
for i in range(q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        heapq.heappush(a, query[1]-offset)
    elif query[0] == 2:
        offset += query[1]
    else:
        print(heapq.heappop(a)+offset)