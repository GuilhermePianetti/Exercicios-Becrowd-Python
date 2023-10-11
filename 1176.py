V = [0, 1]
count = 0
for i in range(60):
    a = V[i] + V[i+1]
    V.append(a)
a = int(input())
while count < a:
    b = int(input())
    print(f'Fib({b}) = {V[b]}')
    count += 1