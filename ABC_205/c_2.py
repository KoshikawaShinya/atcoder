a, b, c = map(int, input().split())

if abs(a) == abs(b):
    print('=')
elif c % 2 == 0:
    if abs(a) > abs(b):
        print('>')
    elif abs(a) < abs(b):
        print('<')
elif c % 2 == 1:
    if a > b:
        print('>')
    elif a < b:
        print('<')