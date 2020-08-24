"""
weight = int(input('Weight: '))
lbsKg = input('(L)bs or (K)g: ')

if lbsKg == 'L':
    print(weight*0.45)
elif lbsKg == 'K':
    print(weight*2.20462262185)
"""

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper == 'L':
   converted = weight * 0.45
   print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} kilos')