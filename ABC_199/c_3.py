n, m = [int(x) for x in input().split()]
city = []
cnt = [[0] * n for i in range(n)]
count = n

for _ in range(m):
    city.append([int(x) for x in input().split()])


count += len(city)
print(count)
