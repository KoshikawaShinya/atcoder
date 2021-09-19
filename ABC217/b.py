w2l = {0:'ABC', 1:'ARC', 2:'AGC', 3:'AHC'}
l2w = {'ABC':0, 'ARC':1, 'AGC':2, 'AHC':3}
cnt = [0]*4

s1 = input()
s2 = input()
s3 = input()

cnt[l2w[s1]] = 1
cnt[l2w[s2]] = 1
cnt[l2w[s3]] = 1

print(w2l[cnt.index(0)])