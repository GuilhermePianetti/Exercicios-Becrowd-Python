X = int(input())
Y = int(input())
soma = 0

if X > Y:
    for i in range(Y+1,X):
        if i %2 != 0:
            soma += i
else:
    for i in range(X+1,Y):
        if i %2 != 0:
            soma += i
print(soma)