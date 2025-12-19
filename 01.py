insts = open("01.txt", "r").read().split("\n")

# PART 1
res = 0
cur = 50
for inst in insts:
    d, n = inst[0], int(inst[1:])
    cur = (cur + (n if d == 'R' else -n)) % 100
    res += cur == 0
print(res)

# PART 2
res = 0
cur = 50
for inst in insts:
    d, n = inst[0], int(inst[1:])
    res += (
        (d == 'R' and cur + n % 100 >= 100)
        + (d == 'L' and cur - n % 100 <= 0 and cur != 0)
        + n // 100
    )
    cur = (cur + (n if d == 'R' else -n)) % 100
print(res)