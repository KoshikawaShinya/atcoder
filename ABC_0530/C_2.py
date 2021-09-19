n, k = [int(x) for x in input().split()]
friend = []
for _ in range(n):
    friend.append([int(x) for x in input().split()])

friend = sorted(friend)

for x in friend:
    if x[0] > k:
        break
    else:
        k += x[1]

print(k)

