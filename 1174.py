count = 0
A = []

while count < 100:
    a = float(input())
    A.append(a)
    count += 1
for i in range(len(A)):
    if A[i] <= 10:
        print(f'A[{i}] = {A[i]}')