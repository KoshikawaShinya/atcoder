n = int(input())
a = [int(x) for x in input().split()]

a[a.index(max(a))] = 0
print(a.index(max(a))+1)


    