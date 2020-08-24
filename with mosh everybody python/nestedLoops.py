for x in range(4):
    for y in range(3):
        print(f'({x,y})')

# bu şekilde iç içe geçmiş döngüler oluşturduk

print('---------------------------------')

"""
CHALLENGE
"""

"""
numbers = [5,2,5,2,2]

çıktı:
xxxxx
xx
xxxxx
xx
xx
"""
# bizden kolayca x le çarpılmasını istenmiyor yoksa bu çıktıya bu yöntemle de ulaşabiliri
# burada iç içe geçmiş döngülerden faydalanmamız lazım

numbers = [5,2,5,2,2]
for m in numbers:
    print('x'*m)

# bu kolay yöntemi
print('------------------------')
# iç içe geçmiş döngüleri kullanarak yapmak

for m in numbers:
    for x in 'x':
        print(x*m)
print('---------------------')
# Öğretmenin yaptığı çözüm:
numbers = [5,2,5,2,2]
for xCount in numbers:
    output = ''
    for count in range(xCount):
        output += 'x'
    print(output)