course = 'Python for begginers'
# len fonksiyonunu kullanarak karakter dizilerimizin kaç ögeden oluştuğunu öğrenebilriz
print(len(course)) 

# methodlara ulaşmak için . noktadan ulaşırız

print(course.upper()) # tüm harfleri büyütür

# eğer methodu kullanarak kalıcı bir işlem yapmak için
# ya tekrardan atama yapmamız lazım ya da yeni den bir değişkene atamak lazım
print(course.lower()) # tüm harfleri küçültür

print(course.find('P')) # P harfinin indeks numarasını bulduk
print(course.find('n')) # n harfinin indeks numarasını bulduk

# Python'da büyük küçük harf duyarlılığı vardır

print(course.replace('begginers','absolute Beginners')) # replace ile karakter dizilerini değiştirebiliriz

# sadece belli bir kısmını değil herhangi bir harfini de değiştirebiliriz
print(course.replace('f','d')) # Python dor beginners

# elimizde bulunan kelimenin bir karakter dizisinde bulunup bulunmadığını kontrol etmek için
# in operatörünü kullanırız

print('Python'in course) # True
print('python' in course) # False (büyük küçük harf duyarlılığı)

"""
course.upper() # tüm harfleri büyüttük
course.lower() # tüm harfleri küçülttük
course.find()  # harfin indeks numarasını ögrendik
course.replace() # harf veya belli parçasını değiştirdik
'...' in course  # course karakter dizinde bulunuyor mu kontrol ettik
"""


