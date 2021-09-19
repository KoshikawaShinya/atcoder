n = int(input())
s = input()
mod = 1000000007
dp = []
for i in range(len(s)+1):
    dp.append([0]*(8))

for i, word in enumerate(s):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if word=='a' and j==0:
            dp[i+1][j+1] += dp[i][j]
        if word=='t' and j==1:
            dp[i+1][j+1] += dp[i][j]
        if word=='c' and j==2:
            dp[i+1][j+1] += dp[i][j]
        if word=='o' and j==3:
            dp[i+1][j+1] += dp[i][j]
        if word=='d' and j==4:
            dp[i+1][j+1] += dp[i][j]
        if word=='e' and j==5:
            dp[i+1][j+1] += dp[i][j]
        if word=='r' and j==6:
            dp[i+1][j+1] += dp[i][j]

    for j in range(8):
        dp[i+1][j] %= mod

print(dp[len(s)][7])



