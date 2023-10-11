m = [[0]*10 for i in range(10)]
n = int(input())
count = 0
while count < n:
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = map(int,input().split())
    if dx <= rx and rx <= cx and dy >= ry and ay <= ry:
        print(1)
    else:
        print(0)
    count += 1