lines = open("12.txt").read().strip().split("\n\n")[-1].split("\n")
res = 0
for line in lines:
    dim, cnt = line.split(": ")
    dim = list(map(int, dim.split("x")))
    cnt = list(map(int, cnt.split()))
    num = (dim[0] // 3) * (dim[1] // 3)
    if num >= sum(cnt):
        res += 1 # i can't believe this actually worked
print(res)