g = list(map(list, open("04.txt", "r").read().split("\n")))
res = 0
remove = True
while remove:
    remove = False
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if col != "@":
                continue
            tot = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(g) and 0 <= nc < len(g[0]):
                        if g[nr][nc] == "@":
                            tot += 1
            if tot < 4:
                res += 1
                g[r][c] = "."
                remove = True
print(res)