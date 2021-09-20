n = int(input())
x, y = map(int, input().split())
dp = []
for i in range(n):
    dp.append([[[float('inf')] for _ in range(y)] for _ in range(x)])

for i in range(n):
    for j in range(x):
        for k in range(y):
            if i == 0:
                dp[0][0][0] = 0
            else:
                a, b = map(int, input().split())
