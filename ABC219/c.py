
def hanten(x):
    vi = ''
    for j in x:
        vi += taka2original[j]
    return vi

x = input()
original2taka = {}
taka2original = {}
for i, a in enumerate(x):
    original2taka[chr(i+97)] = a
    taka2original[a] = chr(i+97)

n = int(input())
vil = []
for i in range(n):
    v = input()
    vil.append(v)
for x in sorted(vil, key=hanten):
    print(x)