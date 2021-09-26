n = int(input())
mod = pow(10, 9) + 7
dice = []
for i in range(n):
    dice.append([int(x) for x in input().split()])

for i in range(n):
    s = sum(dice[i])
    if i == n-1:
        ans = s % mod
    else:
        for j in range(6):
            dice[i+1][j] *= s
print(ans)
