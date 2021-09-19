n, m = [int(x) for x in input().split()]
city = []
cnt = [[0] * n for i in range(n)]
count = n

for _ in range(m):
    city.append([int(x) for x in input().split()])

i=0
while True:
    i += 1
    for j in range(m):
        a = city[i-1][0]
        b = city[i-1][1]
        if b == city[j][0] and a != city[j][1] and [a, city[j][1]] not in city:
            city.append([a, city[j][1]])
    if len(city) <= i:
        break

count += len(city)
print(count)
