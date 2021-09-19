n = int(input())
s = input()

for i, x in enumerate(s):
    if x == '0':
        continue
    else:
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        break
    