def rfn(idx, n):
    # idx : index in bank
    # n   : number of batteries remaining
    # ret : max number that can be created starting from idx with n batteries
    if (idx, n) in mem:
        ret = mem[(idx, n)]
    elif n == 1:
        ret = max(bank[idx:])
    elif len(bank) - idx == n:
        ret = int("".join(map(str, bank[idx:])))
    else:
        ret = 10 ** (n-1) * bank[idx] + rfn(idx + 1, n - 1) # keep
        ret = max(ret, rfn(idx + 1, n))                     # skip
    mem[(idx, n)] = ret
    return ret

res_1, res_2 = 0, 0
banks = open("03.txt", "r").read().split("\n")
for bank in banks:
    mem = {}
    bank = list(map(int, list(bank)))
    res_1 += rfn(0, 2)
    res_2 += rfn(0, 12)
print(res_1, res_2)