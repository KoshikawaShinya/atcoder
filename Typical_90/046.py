n = int(input())
a = [int(x)%46 for x in input().split()]
b = [int(x)%46 for x in input().split()]
c = [int(x)%46 for x in input().split()]
a_cnt = [0] * 46
b_cnt = [0] * 46
c_cnt = [0] * 46

for i in range(n):
    a_cnt[a[i]] += 1
    b_cnt[b[i]] += 1
    c_cnt[c[i]] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a_cnt[i]*b_cnt[j]*c_cnt[k]

print(ans)
