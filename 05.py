ranges, ings = open("05.txt", "r").read().strip().split("\n\n")
ranges = [list(map(int, line.split("-"))) for line in ranges.split("\n")]
ings = list(map(int, ings.split("\n")))
res = 0
for i in range(len(ings)):
    for j in range(len(ranges)):
        if ings[i] >= ranges[j][0] and ings[i] <= ranges[j][1]:
            res += 1
            break
print(res)

ranges.sort()
res = 0
cur = ranges[0]
for r in ranges[1:]:
    if r[0] <= cur[1]:
        cur = [cur[0], max(cur[1], r[1])]
    else:
        res += cur[1] - cur[0] + 1
        cur = r
res += cur[1] - cur[0] + 1
print(res)