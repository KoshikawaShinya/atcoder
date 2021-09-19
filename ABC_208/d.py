import numpy as np
x = 0
a = np.array([])
q = int(input())

for i in range(q):
    query = [int(x) for x in input().split()]
    if len(query) == 2:
        num = query[1]
        qu = query[0]
        if qu == 1:
            print(num)
            np.append(a, num)
        elif qu == 2:
            a = a + num
    elif query[0] == 3:
        print(a.min())
        index = np.argmin(a)
        np.delete(a, index)