# listeler [] köşeli parantezlerle oluşturulur
# hem tanımlarken hem de çıktı ta [] köşeli parantez içinde yazılır

names = ['John','Bob','Mosh','Sarah','Mary']
print(names)
# pythonda her bir ögenin sayısal değerine indeks denir
# indeksler ögeleri daha kolay çağırabilmemizi sağlar
# indeksler 0 dan başlar
# - ile yazılan indeksler sondan başlar
print(names[0])
print(names[3])
print(names[-1])
print(names[-2])

# bölümlendirme
# bölümlendirme 3 adet parametre alabilir
# başlanılacak indeks sayısı : sonlanacak indeks sayısı : atlanacak indeks sayısı

print(names[2:]) # 2. indeksten başlayıp son indekse kadar gitti
# herhangi bir indeks numarası vermezsek tüm ögeleri alır
print(names[:])
# sonlanma indeksi girdiğimizde bir fazlasını yazmak daha doğru olur
# çünkü 4 yazınca aslında makineye 4 e kadar git ama 4 ü dahil etme diyoruz

print(names[2:4]) # mosh, sarah

# indeksleri kullanarak kolayca ögelerin değerlerini değiştirebilir
# silebiliriz
names[0] = 'jon'
print(names)

"""
 Egzersiz
"""
# değişkenin en büyük değerini bulunuz: 
numbers = [3,6,2,8,4,10]
maxDeger = max(numbers)
minDeger = min(numbers)
print(f'numbers değişkenin en büyük değeri {maxDeger}')
print(f'numbers değişkenin en küçük değeri {minDeger}')

# Öğretmenin yaptığı:
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# bu şekilde de bulunur fakat pythonun bize sağladığı özellikleri kullanmak çok daha pratik bir seçenek olacaktır

# bu yolu kullanarak min değerlini bulalım
numbers = [2,5,0,1,100,9]
min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print(min)