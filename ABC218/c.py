n = int(input())
s = []
t = []
ex = ['.'] * n
flag = False

def kaiten(A):
    a = []
    t_a = list(zip(*A))
    for x in t_a[::-1]:
        a.append(x)
    return a
def remov(a):
    f = False
    ind = 0
    for i, x in enumerate(a):
        if '#' in x:
            ind = i
            break
    a = a[ind:]
    a = a[::-1]
    for i, x in enumerate(a):
        if '#' in x:
            ind = i
            break
    a = a[ind:]
    return a

for i in range(n):
    s.append([x for x in input()])
for i in range(n):
    t.append([x for x in input()])
s = remov(s)
t = remov(t)
s = kaiten(s)
t = kaiten(t)
s = remov(s)
t = remov(t)
for i in range(4):
    if s == t:
        flag = True
    t = kaiten(t)
if flag:
    print('Yes')
else:
    print('No')