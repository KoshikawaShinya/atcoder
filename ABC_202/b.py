num = input()
rev = {"0":"0", "1":"1", "6":"9","8":"8", "9":"6"}
a = ""

num = num[::-1]
for x in num:
    a += rev[x]
print(a)
