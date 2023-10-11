A=0
B = 1
for i in range(1,40,2):
    A = float(A + i / B)
    B = B * 2
print('{:.2f}'.format(A))