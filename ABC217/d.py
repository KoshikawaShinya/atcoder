import numpy as np

def idx_of_the_nearest(data, value):
    idx = np.argmin(np.abs(np.array(data) - value))
    return idx

l, q = map(int, input().split())
cut = [0]
offset = 0

for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        cut.append(x)
    elif c == 2:
        idx = idx_of_the_nearest(cut, x)
        near = cut[idx]
        if near < x and idx+1 < len(cut):
            tmp_idx = idx_of_the_nearest(cut[idx+1:], x)
            tmp = cut[tmp_idx]
        elif near > x and idx-1 >= 0:
            tmp_idx = idx_of_the_nearest(cut[:idx], x)
            tmp = cut[tmp_idx]
        elif idx+1 == len(cut):
            tmp = l
        elif idx-1 == -1:
            tmp = 0
        print(cut)
        print(near, tmp)
        print(abs(near-tmp))
