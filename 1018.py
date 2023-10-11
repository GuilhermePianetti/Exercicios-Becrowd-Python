VL = int(input())

n100 = VL // 100
VLV = VL - (100 * n100)

n50 = VLV // 50
VLV = VLV - (50 * n50)

n20 = VLV // 20
VLV = VLV - (20 * n20)

n10 = VLV // 10
VLV = VLV - (10 * n10)

n5 = VLV // 5
VLV = VLV - (5 * n5)

n2 = VLV // 2
VLV = VLV - (2 * n2)

n1 = VLV

print(VL)
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")