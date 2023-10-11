A,B = map(int,input().split())

if A>B:
    print("O JOGO DUROU", 24-A+B, "HORA(S)")
elif B>A:
    print("O JOGO DUROU", B-A, "HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")