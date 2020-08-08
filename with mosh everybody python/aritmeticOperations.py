# sayılarla işlemler yapmak için matematik operatörlerinden faydalanırız

# + - * / // % 

# toplama operatörü +
print(20 + 10)

# çıkarma operatörü
print(20-5)

# çarpma operatörü
print(15 * 3)

# bölme operatörü / 
print(20 / 10) # 2.0
# bu bölme operatörü float bir değer verir

# bölme operatörü //
print(20 // 10) # 2
# bu bölme operatörü tam bir değer verir

# değişkenin değeriyle matematik işlemleri

x = 10

# uzun yöntemi
x = x + 10
print(x) # 20

# kısa yöntemi
x += 10
print(x) # 30

y = 10

# çıkarma
y -= 5
print(y)

# çarpma
y *= 3
print(y)

# matematikte ki işlem öncelliği python da geçerlidir
x = 10 + 3 * 2
print(x) # önce çarpma sonra toplama

# parantez içine aldığımız işlemler önceliğe sahiptir
x1 = (2+3) * 10-3
print(x1)


# sayıları yuvarlamaka

# sayıları yuvarlamak için round() fonksiyonundan yararlanırız

x = 3.9
print(round(x)) # 4

# sayıları negatif sayıdan pozitif sayıya çevirmek için abs() fonksiyonundan yararlanırız

x = - 2.9
print(abs(x))
x1 = - 100
print(abs(x1))

## modül içeri aktarma

import math
print(math.ceil(2.9)) # 3

print(math.ceil(1.2))
print(math.ceil(5.3))

# ceil modülü bir üst sayıya çıkartır

print(math.floor(25.65)) # 25
# floor modülü bir alt sayıya döndürür