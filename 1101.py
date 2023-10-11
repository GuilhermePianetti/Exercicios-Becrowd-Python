M,N = map(int,input().split())
soma = 0

if N > M:
    for i in range(M,N+1):
            print('%d '%(i),end="")
            soma+=i
            if i == N:
                print('Sum=%d'%(soma))
else:
    for i in range(N,M+1):
            print('%d '%(i),end="")
            soma+=i
            if i == M:
                print('Sum=%d'%(soma))