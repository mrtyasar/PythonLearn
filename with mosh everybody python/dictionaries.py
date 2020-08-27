# sözlükler

# sözlükler bildiğimiz sözlüklerin işlevini yerine getirir
# bir anahtar kelimemiz ve bir değeri vardır
# book : kitap gibi

customer = {
    'name':'john Smith',
    'age':30,
    'is verified':'True'
}

# değere erişmek için anahtar kelimesini kullanmamız lazım

print(customer['name'])

# eğer sözlükte bulunmayan bir anahtar kelimeyi çağırırsak keyError hatası alırız
#print(customer['Falan']) # KeyError: 'Falan'

# eğer hata almak istemiyorsak ta get methodunu kullanarakta ögeleri çağırabiliriz
print(customer.get('Falan')) # None

# değerleri güncelleyebiliriz
customer['age'] = 45
print(customer['age']) #45

# değer ekleyebiliriz
customer['birthdate'] = 'Jan 1 1980'
print(customer)


"""
Egzersiz

:: phone: 1234

output = One, Two, Three, Four

"""

phone = input('Phone: ')
digits = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four'
}
output = ''
for ch in phone:
    output += digits.get(ch,'!') + ' '
print(output)
