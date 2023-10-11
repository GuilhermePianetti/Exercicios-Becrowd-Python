s = 0
count = 0

while True:
    w1,w2,r = map(float, input().split())
    if w1!=0 and w2!=0 and r!=0:
        
        m = (w1*(1+(r/30)) + w2*(1+(r/30))) / 2
        s += m
        count += 1
        if 1 <= m < 13:
            print('Nao vai da nao')
        elif 13 <= m < 14:
            print('E 13')
        elif 14 <= m < 40:
            print('Bora, hora do show! BIIR!')
        elif 20 <= m <= 60:
            print('Ta saindo da jaula o monstro!')
        else:
            print('AQUI E BODYBUILDER!!')
    else:
        break
if s/count > 40:
    print("\nAqui nois constroi fibra rapaz! Nao e agua com musculo!")