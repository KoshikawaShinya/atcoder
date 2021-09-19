dice = [int(x) for x in input().split()]
mul = 0

for x in dice:
    mul += 7 - x

print(mul)
