n, k = [int(x) for x in input().split()]
friend = []
point = 0
fri_p = 0
cnt = 0

for _ in range(n):
    friend.append([int(x) for x in input().split()])


while True:
    if k > 0:
        point += 1
        k -= 1
        for x in friend:
            if x[0] == point:
                k += x[1]
                cnt += 1
        if cnt >= len(friend):
            point += k
            break
    else:
        break

print(point)
