S = int(input())
H = 0
M = 0


H = S // 3600
R = S - (H*3600)
M = R // 60
S = R - (M * 60)
print(f"{H}:{M}:{S}")
