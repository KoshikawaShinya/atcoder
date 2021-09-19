fig = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

s = input()
s = s[::-1]
kai_s = ""

for st in s:
    kai_s += fig[st]

print(kai_s)