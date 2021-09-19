def summax(x):
    a = 0
    for i in x:
        a += i
    return a
def ymax(x):
    return x[1]
def xmax(x):
    return x[0]

n = int(input())
x, y = map(int, input().split())
bentou = []
for i in range(n):
    bentou.append([int(v) for v in input().split()])

bentou_sumsort = sorted(bentou, key=summax)
count = 0
for i in range(n):
    ben = bentou_sumsort.pop()
    a, b = ben
    x -= a
    y -= b
    count += 1
    if x <= 0 and y <= 0:
        break
    elif x <= 0 and y > 0:
        bentou = sorted(bentou_sumsort, key=ymax)
        while len(bentou) >= 1:
            j = bentou.pop()
            y-= j[1]
            count += 1
            if y <= 0:
                break
        break
    elif y <= 0 and x > 0:
        bentou = sorted(bentou_sumsort, key=xmax)
        while len(bentou) >= 1:
            j = bentou.pop()
            x-= j[0]
            count += 1
            if x <= 0:
                break
        break
if x <= 0 and y <= 0:
    print(count)
else:
    print(-1)

