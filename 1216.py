S = 0
count = 0
while True:
    try:
        N = str(input())
        D = int(input())
        S += D
        count += 1
    except EOFError:
        break
print('%.1f' % (S/count))