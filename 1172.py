count = 0
X = []

while count < 10:
    a = int(input())
    X.append(a)
    count += 1
for i in range(len(X)):
    if X[i] <=0:
        X[i] = 1
    print(f'X[{i}] = {X[i]}')