# liste methotları listelerimiz üzerine methotlar sayesinde işlemler yapmamızı sağlar
numbers = [5,2,1,7,4]
# listeye öğe eklemek için append methodundan yararlanırız
numbers.append(20)
print(numbers)

# listeye indeks numarasına göre öge eklemek
numbers.insert(2,10)
print(numbers)

# listemizde bir öğeyi silmek için remove methodundan yararlanırız
numbers.remove(5)
print(numbers)

# listemizdeki tüm ögeleri silmek için clear() methodundan yararlanırız
numbers.clear()
print(numbers) # []

number = [1,2,3,4,3,5]

# listenin son ögesini silmek için pop() methoundan yararlanırız
number.pop()
print(number) # [1,2,3,4]

# listedeki ögelerin varlığını ögrenmek için methotlardan yararlanabiliriz

# index() methodu sayesinde öğenin listedeki indeks sayısını öğrenmiş olduk
print(number.index(2)) #1

# index() methoduna listede bulunmayan bir öğeyi yazarsak ValueError hatası alırız

# bir değerin listede bulunup bulunmadığını in kelimesini kullanarak bulabiliriz

print(2 in number) # 2 değeri number listesinde bulunduğu için değer True oldu
print(100 in number) # 100 değeri number listesinde bulunduğu için değer False oldu

# bir değerin listenin içinde kaç tane bulunduğunu kontrol etmek için count() methodunu kullanırız
print(number.count(3)) #2
print(number.count(4)) # 1
print(number.count(40)) # bulunmadığı için 0

# listeleri küçükten büyüğe sıralamak için sort() methodundan yararlanabiliriz
number.sort()
print(number) # [1,2,3,3,4]

# listeleri büyükten küçüğe sıralamak için reverse() methodundan yararlanırız
number.reverse()
print(number) # [4,3,3,2,1]

# listemizin bir kopyasını almak için copy() methodundan yararlanırız
number2 = number.copy()
number.append(10)
print(number) # [4,3,3,2,1,10]
print(number2) # [4,3,3,2,1]

# listemizin bir kopyasını almak, listeye sonradan ekleyeceğimiz, çıkartacağımız vb.
# gibi değişikliklerden etkilenmemesi için en doğru yoldur


"""
EGZERSİZ
"""

# bir listemiz var bu listenin içinde aynı değere sahip 1 den fazla öge var
# bu ögelerin kopyalarını nasıl silebiliriz

numbersOne = [2,2,4,6,3,4,6,1] 
uniques = [] # boş bir liste
for numberTwo in numbersOne: # numbersOne listesindeki her bir ögeye numberTwo adını verdik:
    if numberTwo not in uniques: # eğer öge uniques listesinde yok ise:
        uniques.append(numberTwo) # uniques listesine o ögeyi ekle
print(uniques) # [2,4,6,3,1] # uniques listesini yazdır

"""
numbersOne adlı değişkenin içinde kopyalarıda bulunan karışık değerli bir listemiz var
bu listedeki kopyalardan arınmış halini uniques listesinde toplayacağız
bu yüzden boş bir liste yarattık
numberOne daki her bir ögeyi ele aldık
eğer dedik numberTwo ögeleri uniques içinde yok ise bu listeye ögeyi ekle dedik
not in dememizin sebebi eğer 1 uniques in içinde ise bir daha birin yazılmasını engellemek
bu sayede listenin kopyalardan arınmış halini oluşturduk
"""



