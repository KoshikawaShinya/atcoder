from collections import Counter
n, k = map(int, input().split())
a = list(map(int,input().split()))

c = Counter()

ans = 0
left = right = 0
while right < n:
    c[a[right]] += 1
    while left <= right and len(c.keys()) > k:
        c[a[left]] -= 1
        if c[a[left]] == 0:
            del c[a[left]]
        left += 1
    ans = max(ans, right - left + 1)
    right += 1

print(ans)