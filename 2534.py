v = []
n, c = map(int,input().split())
for i in range(n):
    a = int(input())
    v.append(a)
for i in range(n):
        for j in range(0, n-i-1):
            if v[j] < v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
for i in range(c):
     q = int(input())
     print(v[q-1])