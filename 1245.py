while True:
    try:
        n = int(input())
        count = 0
        b = [[0]*n for i in range(2)]
        for i in range(n):
            m, l = input().split()
            if l == "E":
                b[0][i] = m
            else:
                b[1][i] = m
        for i in range(n):
            for j in range(n):
                if b [1][i] != 0:
                    if b[0][i] == b[1][j]:
                        count += 1
                        b[0][i] = 0
                        b[1][j] = 0
                        break
        print(count)
    except EOFError:
        break
    except RuntimeError:
        break