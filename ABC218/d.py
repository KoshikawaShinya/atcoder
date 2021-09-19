n = int(input())
zahyo = []
zi = {}
for i in range(n):
    zahyo.append([int(x) for x in input().split()])
    zi[str(zahyo[i])] = i
zahyo.sort()
count = 0
for i in range(n):
    for j in range(i, n):
        if zahyo[i][0] < zahyo[j][0] and zahyo[i][1] < zahyo[j][1]:
            p_1 = str([zahyo[i][0], zahyo[j][1]])
            p_2 = str([zahyo[j][0], zahyo[i][1]])
            if p_1 in zi and p_2 in zi:
                count += 1
print(count)
