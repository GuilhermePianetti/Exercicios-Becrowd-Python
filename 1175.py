count = 0
N = []
### mudar para 20
while count < 20:
    a = int(input())
    N.append(a)
    count += 1
for i in range((len(N))//2):
    ###trocar para 20
    a = N[19-i]
    N[19-i] = N[i]
    N[i] = a
for i in range(len(N)):
    print(f'N[{i}] = {N[i]}')