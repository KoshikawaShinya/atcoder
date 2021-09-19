n, y = [int(x) for x in input().split()]
count = 0

for i in range(n + 1):
    for j in range(n + 1):
        count = i + j
        if count > n:
            break

        mul = 1000*(n-i-j) + 5000*j + 10000*i
        if mul == y:
            print("{} {} {}".format(i, j, n-i-j))
            exit()
    

print("-1 -1 -1")
