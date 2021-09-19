import numpy as np
import bisect


l, q = map(int, input().split())
cut = [0]
offset = 0

for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        cut.append(x)
        cut.sort()
    elif c == 2:
        idx = idx_of_the_nearest(cut, x)
        near = cut[idx]
        if idx+1 < len(cut) and idx-1 >= 0:
            tmp_idx = idx_of_the_nearest(cut[:idx]+cut[idx+1:], x)
            tmp = cut[tmp_idx]
        elif idx+1 == len(cut):
            tmp = l
        elif idx-1 == -1:
            tmp = 0
        print(cut)
        print(near, tmp)
        print(abs(near-tmp))