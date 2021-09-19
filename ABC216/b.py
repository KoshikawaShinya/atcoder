n = int(input())
name = []
flag = False
for i in range(n):
    name.append([x for x in input().split()])

for a, i in enumerate(name):
    for j in name[a+1:]:
        if i == j:
            flag = True
            break
    if i == j:
        break
if flag:
    print('Yes')
else:
    print('No')