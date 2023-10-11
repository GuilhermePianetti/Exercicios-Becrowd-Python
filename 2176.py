messagem = input()
um = 0

for i in messagem:
    if i == '1':
        um += 1

print(messagem + str(um % 2))