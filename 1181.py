m = [[0]*12 for i in range(12)]

l = int(input())
t = input()

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = float(input())

if t == "s":
    s = 0
    for j in range(len(m[l])):
        s += m[l][j]
    print(s)
else:
    med = 0
    for j in range(len(m[l])):
        med += m[l][j]
    med = med / len(m[l])
    print(med)