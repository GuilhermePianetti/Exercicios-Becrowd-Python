t = int(input())

for i in range(t):
    g, q = map(int, input().split())

    if g > q:
        a = g // q
        g = g - (q * a)
        g += a
    
    print(g)