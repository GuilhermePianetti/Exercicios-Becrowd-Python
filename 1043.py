A,B,C = map(float,input().split())


if (B + C) > A and (A + C) > B and (A + B) > C:
    print('Perimetro =', A+B+C)
else:
    print('Area =', ((A+B) * C) /2)