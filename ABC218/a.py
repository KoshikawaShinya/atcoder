n = int(input())
s = input()

for i in range(len(s)):
    if i+1 == n:
        if s[i] == 'o':
            print('Yes')
        elif s[i] == 'x':
            print('No')