import math

def lcm(a, b):
    x = a * b // math.gcd(a, b)
    return int(x)
a, b = map(int, input().split())
m = 10**18

l = lcm(a, b)
if l <= m:
    print(l)
else:
    print('Large')