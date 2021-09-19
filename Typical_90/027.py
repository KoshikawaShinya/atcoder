n = int(input())
reg = set()
for i in range(n):
    s = input()
    if s in reg:
        continue
    reg.add(s)
    print(i+1)

