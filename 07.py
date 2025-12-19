g = open("07.txt").read().split("\n")
sp = {}
for r, row in enumerate(g):
    for c, char in enumerate(row):
        if char == "S":
            s = (r, c)
        elif char == "^":
            sp[(r, c)] = 0
mem = set()
def rfn(r, c):
    if (r, c) in mem:
        return
    mem.add((r, c))
    if r > len(g):
        return
    if (r, c) in sp and sp[(r, c)] == 0:
        sp[(r, c)] = 1
        rfn(r, c + 1)
        rfn(r, c - 1)
    else:
        rfn(r + 1, c)
rfn(s[0], s[1])
print(sum(sp.values()))

mem = {}
def rfn2(r, c):
    if (r, c) in mem:
        return mem[(r, c)]
    if r > len(g):
        return 1
    if (r, c) in sp:
        res = rfn2(r, c + 1) + rfn2(r, c - 1)
    else:
        res = rfn2(r + 1, c)
    mem[(r, c)] = res
    return res
print(rfn2(s[0], s[1]))