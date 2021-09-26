import math
h, w = map(int, input().split())
if w==1 or h==1:
    print(h*w)
else:
    h = math.ceil(h/2)
    w = math.ceil(w/2)
    print(h*w)