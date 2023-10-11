A = float(input(''))
B = float(input(''))

while A < 0 or A > 10:
   A = float(input())

while B < 0 or B > 10:
   B = float(input())

MEDIA = ((A * 3.5) + (B * 7.5)) / 11
(print('MEDIA = '"%.5f" % MEDIA))
