n = int(input())
command = []
while n > 0:
    if n % 2 == 0:
        n = n // 2
        com = 'B'
    else:
        n -= 1
        com = 'A'

    command.append(com)
command.reverse()
print(''.join(command))