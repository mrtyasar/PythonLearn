birthYear = input('Birth year: ')
print(type(birthYear)) # değişkenin tipini öğrendik
age = 2020 - int(birthYear) # değişkeni int veri tipine çevirdik
print(type(age)) # değişkenin tipini öğrendik
print(age)

# Egzersiz

weightLbs = input('Weight (lbs): ')
weightKg = int(weightLbs) * 0.45
print(weightKg)