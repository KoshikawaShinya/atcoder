n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
cnt_a = 0
cnt_b = 0
sa = 10**9
a.sort()
b.sort()

for i in range(n+m):
    tmp = abs(a[cnt_a]-b[cnt_b])
    if sa > tmp:
        sa = tmp
    
    if cnt_a == n-1 or cnt_b == m-1:
        break
    if a[cnt_a] < b[cnt_b] and cnt_a < n-1:
        cnt_a += 1
    elif a[cnt_a] > b[cnt_b] and cnt_b < m-1:
        cnt_b += 1
    elif a[cnt_a] == b[cnt_b]:
        sa = 0
        break
    

print(sa)