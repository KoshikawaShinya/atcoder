n = int(input())

for i in range(2**n):
    a = format(i, 'b').zfill(n)
    b = a
    for j in range(n):
        if '01' in a:
            a = a.replace('01', '')
        else:
            break
    if len(a) == 0:
        b = b.replace('0', '(')
        b = b.replace('1', ')')
        print(b)

