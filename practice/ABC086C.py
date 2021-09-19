n = int(input())
plan = []
flag = True
x_old, y_old, t_old = 0, 0, 0

for i in range(n):
    plan.append([int(x) for x in input().split()])

for t, x, y in plan:
    d = x + y
    if t >= d:
        if (t-d) % 2 != 0 or (t-t_old) < abs(x - x_old)+abs(y-y_old):
            flag = False
            break
        x_old = x
        y_old = y
        t_old = t
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
