sal = float(input())

if 0 <= sal <= 400.00:
    salf = sal * 1.15
elif 400.01 <= sal <= 800.00:
    salf = sal * 1.12
elif 800.01 <= sal <= 1200.00:
    salf = sal * 1.10
elif 1200.01 <= sal <= 2000.00:
    salf = sal * 1.07
else:
    salf = sal * 1.04
print("Novo salario:", "%.2f" % salf)
print("Reajuste ganho:", "%.2f" % (salf - sal))
print("Em percentual:", ("%.0f" % (((salf * 100) / sal) - 100)), "%") 