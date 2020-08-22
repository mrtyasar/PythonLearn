isHot = True

if isHot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day!")


# eğer değer false olsaydı kod çalışmayacaktı

isHot1 = False

if isHot1:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day!")

# isHot1 False bir değer olduğu için if bloğu çalışmadı
# Enjoy your day ifadesinin çalışmasının sebebi if bloğun dışında olmasındandır

print('------------------------------------')

# else 

# eğer if bloğu koşulu sağlamıyorsa en son hiçbir koşul gözetmeksizin çalışmasını
# istediğimiz kodları else bloğuna yazarız

isHot = True
isCold = False
if isHot:
    print("It's a hot day")
    print("Drink plenty of water")
elif isCold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")

print('----------------------------')
print('    EGZERSİZ     ')
print('----------------------------')


price = 1000000
goodCredit = True
if goodCredit:
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
print(f"Down payment: ${downPayment}")

