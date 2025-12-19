lines = [s.split(": ") for s in open("11.txt").read().strip().split("\n")]
adj = {s[0]: s[1].split() for s in lines}

# PART 1
mem = {}
def rfn(node):
    if node in mem:
        return mem[node]
    if adj[node] == ["out"]:
        return 1
    res = 0
    for nxt in adj[node]:
        res += rfn(nxt)
    mem[node] = res
    return res
print(rfn("you"))

# PART 2
mem = {}
def rfn2(node, fft_flag, dac_flag):
    if (node, fft_flag, dac_flag) in mem:
        return mem[(node, fft_flag, dac_flag)]
    if adj[node] == ["out"]:
        return int(fft_flag and dac_flag)
    res = 0
    for nxt in adj[node]:
        res += rfn2(nxt, fft_flag or nxt == "fft", dac_flag or nxt == "dac")
    mem[(node, fft_flag, dac_flag)] = res
    return res
print(rfn2("svr", False, False))