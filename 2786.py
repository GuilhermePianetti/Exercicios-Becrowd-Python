t1 = 0
t2 = 0
l = int(input())
c = int(input())

if l == c and l == 1:
    t1 += 1
else:
    t2 = 2*((l-1)+(c-1))
    t1 = l*c + (l-1)*(c-1)
print(t1)
print(t2)