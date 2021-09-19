def mat_minus(d, b):
    a = d[0] - b[0]
    c = d[1] - b[1]
    return [a, c]
def mat_fig(a):
    if a[0] < 0 and a[1] < 0:
        return True
    else:
        return False

n = int(input())
x, y = map(int, input().split())
dp = [[[0, 0]]*(n+1) for x in range(n+1)]
bentou = []
for i in range(n):
    bentou.append([int(v) for v in input().split()])
    dp[i][0] = [x, y]

for i in range(n):
    bentou_tmp = bentou[:i]+bentou[i+1:]
    for j in range(1, n):
        dp[i][j] = mat_minus(dp[i][j-1], bentou_tmp[j-1])
        print(dp)
        if mat_fig(dp[i][j]):
            print(mat_fig(dp[i][j]))
            print(i+1)
            exit()

print(-1)
