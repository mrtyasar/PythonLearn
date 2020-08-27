# parametreler fonksiyonlara değer olarak verdiğimiz argümanlara denir
print('Merhaba!')
# burada print() bir fonksiyon 'Merhaba!' değeri ise bir parametredir

# yarattığımız fonksiyonlara parametre girilmesini nasıl sağlayabiliriz:

def selamlama(name):
    print('Selamlar!')
    print(f'Hoşgeldin {name}!')

print('Start')
selamlama('John')
print('Finish')

# eğer birden fazla parametre istiyorsak fonksiyonu yaratırken bunu belirtmeliyiz

def selam(name,surname):
    print('Selamlar!')
    print(f'Hoşgeldiniz {name} {surname}!')

print('Start')
selam('John','Wick')
print('Finish')