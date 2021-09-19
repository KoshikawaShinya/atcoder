import numpy as np

h, w, n = map(int, input().split())
card = []
a_ = np.array([])
b_ = np.array([])
for i in range(n):
    a, b = map(int, input().split())
    a_ = np.append(a_, a)
    b_ = np.append(b_, b)
    card.append([a, b])

a_ = list(a_.argsort())
b_ = list(b_.argsort())

for i in range(n):
    a_min = a_[i]
    b_min = b_[i]

    card[a_min][0] = i+1
    card[b_min][1] = i+1

for i in card:
    print(i[0], i[1])