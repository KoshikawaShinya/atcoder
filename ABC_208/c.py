n = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a = sorted(a)
b = sorted(b)
c = 1000000000
index_a = 0
index_b = 0
for i in range(len(a) + len(b) - 1):
    a_tmp = a[index_a]
    b_tmp = b[index_b]
    tmp = abs(a_tmp - b_tmp)
    if c > tmp:
        c = tmp
    if a_tmp > b_tmp:
        if index_b < len(b)-1:
            index_b += 1
        elif index_b == len(b)-1:
            index_a += 1
    elif a_tmp < b_tmp:
        if index_a < len(a)-1:
            index_a += 1
        elif index_a == len(a)-1:
            index_b += 1
    else:
        break
print(c)