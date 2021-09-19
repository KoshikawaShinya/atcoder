n, a, x, y = map(int, input().split())

if n <= a:
    print(n*x)
else:
    b = n-a
    print(a*x + b*y)