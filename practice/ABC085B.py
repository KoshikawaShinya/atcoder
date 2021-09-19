n = input()
d = []
mochi = 0
count = 0

for i in range(int(n)):
    d.append(input())
d.sort()
d = list(set(d))

print(len(d))
