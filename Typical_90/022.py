a, b, c = map(int, input().split())

def euclid(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x % y
        elif x < y:
            y = y % x
    return max(x, y)

r = euclid(a, euclid(b, c))
print(a//r+b//r+c//r-3)