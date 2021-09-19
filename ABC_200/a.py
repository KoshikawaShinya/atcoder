n = int(input())

a = n / 100
b = n // 100

if a > b:
    print(int(a+1))
else:
    print(int(a))