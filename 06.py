g = [row.split() for row in open("06.txt").read().strip().split("\n")]
res = 0
for col in range(len(g[0])):
    op = g[-1][col]
    cur = int(g[0][col])
    for row in range(1, len(g)-1):
        match op:
            case "*": cur *= int(g[row][col])
            case "+": cur += int(g[row][col])
    res += cur
print(res)

g = [list(row) for row in open("06.txt").read().split("\n")]
res = 0
accum = []
for col in range(len(g[0])-1, -1, -1):
    num = ""
    for row in range(len(g)):
        if g[row][col].isdigit():
            num += g[row][col]
        elif g[row][col] in "+*":
            accum.append(int(num))
            print(accum)
            run = accum[0]
            for x in accum[1:]:
                match g[row][col]:
                    case "+": run += x
                    case "*": run *= x
            res += run
            accum = []
            break
    else:
        if num:
            accum.append(int(num))
print(res)