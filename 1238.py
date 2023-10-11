n = int(input())

for _ in range(n):
    a, b = input().split()
    v1 = list(a)
    v2 = list(b)
    v3 = []

    c = min(len(v1), len(v2))
    d = max(len(v1), len(v2))

    for i in range(c):
        v3.append(v1[i])
        v3.append(v2[i])

    if len(v1) > len(v2):
        v3 += v1[c:d]
    else:
        v3 += v2[c:d]

    print(''.join(v3))
