import re
r = open("02.txt", "r").read().split(",")
res_1, res2 = 0, 0
for interval in r:
    l, h = map(int, interval.split("-"))
    for i in range(l, h+1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            res_1 += i
        if re.match(r"^(\d+)\1+$", s):
            res_2 += i
print(res_1, res_2)