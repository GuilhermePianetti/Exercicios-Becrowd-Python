V = int(input())
A = 0
B = 1

for i in range (0,V):
    if i == V-1:
        print(A)
    else:
         print(A, end=" ")
    C = A + B
    A = B
    B = C