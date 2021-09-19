n = int(input())
one = [0] * (n+1)
two = [0] * (n+1)
for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        one[i+1] = one[i]+p
        two[i+1] = two[i]
    if c == 2:
        one[i+1] = one[i]
        two[i+1] = two[i]+p
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(one[r]-one[l-1], two[r]-two[l-1])