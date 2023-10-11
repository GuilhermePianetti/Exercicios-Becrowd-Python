I = float(input())
VV = 1000 * 0.08
VV2 = 1500 * 0.18

if I <= 2000:
    tx = "Isento"
elif I > 2000 <= 3000:
    tx = (I - 2000) * 0.08
elif I > 3000 <= 4500:
    tx = ((I - 3000) * 0.18) + VV
else:
    tx = ((I - 4500) * 0.28) + VV + VV2
print("R$ " "%.2f" % tx)