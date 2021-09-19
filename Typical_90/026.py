n = int(input())
neigh_mat = []
for i in range(n):
    neigh_mat.append([0]*n)

for i in range(n):
    a, b = map(int, input().split())
    neigh_mat[a][b] += 1
    neigh_mat[b][a] += 1
    neigh_mat[a][a] += 1
    neigh_mat[b][b] += 1
