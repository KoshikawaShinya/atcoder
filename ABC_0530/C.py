n, k = [int(x) for x in input().split()]
friend = []
friend_next = [[0, 0]]
point = 0
fri_p = 0

for _ in range(n):
    friend.append([int(x) for x in input().split()])


while True:
    if k > 0:
        point += 1
        k -= 1
        if len(friend) - 1 < fri_p:
            point += k
            break
        elif point == friend[fri_p][0]:
            k += friend[fri_p][1]
            fri_p += 1
    else:
        break

print(point)
