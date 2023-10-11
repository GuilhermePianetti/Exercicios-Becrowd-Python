a = int(input())
N = [a]
for i in range(10):
    b = a*2
    N.append(b)
    a = b
    print(f'N[{i}] = {N[i]}')