import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())
for i in range(q):
    time = int(input())
    rad = time / t
    rad = 2*math.pi * rad
    za = [0, -(l/2)*math.cos(rad+math.pi*(3/2)), l/2+(l/2)*math.sin(rad+math.pi*(3/2))]
    direct = math.sqrt(x**2 + (y-za[1])**2)
    fukaku = math.atan(za[2]/direct)

    print(math.degrees(fukaku))