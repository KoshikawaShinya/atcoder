n = input()

for i in range(10):
    t = '0'*i + n
    if t == t[::-1]:
        print('Yes')
        exit()
print('No')

