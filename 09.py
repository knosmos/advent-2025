pos = [list(map(int, p.split(","))) for p in open("09.txt").read().strip().split("\n")]
opt = 0
for i, p1 in enumerate(pos):
    for p2 in pos[i+1:]:
        dx = p1[0] - p2[0] + 1
        dy = p1[1] - p2[1] + 1
        area = abs(dx * dy)
        opt = max(opt, area)
print(opt)

opt = 0
for i, p1 in enumerate(pos[:-1]):
    for p2 in pos[i+1:]:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        area = (abs(dx)+1) * (abs(dy)+1)
        if area <= opt:
            continue
        # print("checking", p1, p2, area)
        valid = True
        # check if any other points are inside the rectangle
        for p in pos:
            if p == p1 or p == p2:
                continue
            if min(p1[0], p2[0]) < p[0] < max(p1[0], p2[0]) and min(p1[1], p2[1]) < p[1] < max(p1[1], p2[1]):
                valid = False
                break
        if not valid:
            # print("reject inside")
            continue
        # check all edges to see if any cross the rectangle
        for j, pa in enumerate(pos):
            for pb in pos[j+1:]:
                ax, ay = pa
                bx, by = pb
                if ax == bx: # vertical
                    if min(p1[0], p2[0]) < ax < max(p1[0], p2[0]) and \
                        ((ay <= min(p1[1], p2[1]) and by >= max(p1[1], p2[1])) or
                         (by <= min(p1[1], p2[1]) and ay >= max(p1[1], p2[1]))):
                        valid = False
                        # print("reject v", pa, pb)
                        break
                if ay == by:
                    if min(p1[1], p2[1]) < ay < max(p1[1], p2[1]) and \
                        ((ax <= min(p1[0], p2[0]) and bx >= max(p1[0], p2[0])) or
                         (bx <= min(p1[0], p2[0]) and ax >= max(p1[0], p2[0]))):
                        valid = False
                        # print("reject h", pa, pb)
                        break
        # check next to make sure direction is correct
        nxt = pos[i+1]
        if nxt[0] - p1[0] > 0 and dy < 0:
            # print("reject x+")
            valid = False
        if nxt[0] - p1[0] < 0 and dy > 0:
            # print("reject x-")
            valid = False
        if nxt[1] - p1[1] > 0 and dx > 0:
            # print("reject y+")
            valid = False
        if nxt[1] - p1[1] < 0 and dx < 0:
            # print("reject y-")
            valid = False

        if valid:
            print(p1, p2, area)
            opt = max(opt, area)
print(opt)