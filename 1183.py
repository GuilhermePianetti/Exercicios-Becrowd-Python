m = [[0]*12 for i in range(12)]
o = input()
count = 1
s = 0
q = 0

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] = float(input())

for i in range(len(m)-1):
    for j in range(count, len(m[i])):
        s += m[i][j]
        q += 1
    count += 1

if o == "S":
    print(s)

else:
    med = s/q
    print("%.1f" % med)