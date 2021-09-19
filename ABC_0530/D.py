n, k = [int(x) for x in input().split()]
a = []
center = k**2 // 2 + 1
col = []
mini = 800**2

def convert(x, cols):
    return [x[i:i + cols] for i in range(0, len(x), cols)]

for _ in range(n):
    a.append([int(x) for x in input().split()])

for m_i in range(k):
    for m_j in range(k):
        for i in range(k):
            for j in range(k):
                col.append(a[i+m_i][j+m_j])
        
        if i == n-1:
            break
    if i == n-1:
        break
        
col = convert(col, k**2)

for x in col:
    x = sorted(x, reverse=True)
    if mini > x[center-1]:
        mini = x[center-1]

print(mini)
