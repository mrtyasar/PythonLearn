def sem(number):
    print(number * number)

print(sem(20))

# değişkene atayarakta yazdırabiliriz
result = sem(30)
print(result)
sem(10)

def isminNe():
    isim = input('İsmin ne? ')
    print(isim)

print('Merhaba {}. Nasılsın?'.format(isminNe())) # Merhaba None. Nasılsın?

# istenilen çıktıyı alamadık:

def nameOr():
    name = input('İsmin ne?')
    return name

print('Merhaba {}. Nasılsın?'.format(nameOr())) # Merhaba murat. Nasılsın?

# pythonda return dan sonra gelen kodları okumaz mesala:

def mesala():
    print(5)
    print(10)
    return
    print(3)

mesala() # 5 ile 10 u yazdırdı fakat 3 return dan sonra geldiği için yazılmadı

# bu özelliği çeşitli şekillerden yararlanabiliriz
# mesala bu bu olmazsa diğer kodları önemseme diye

def fonk(n):
    if n < 0:
        return 'eksi değerli sayı olmaz!'
    else:
        return n

f = fonk(-5)
print(f)

# kısaca:
# eğer biz return yerine print() fonksiyonunu kullansaydık bir çok önemli işlevi
# sadece print() fonksiyonu ile sınırlandırmış olurduk

# return ifadesi ile işlem yaptığımızda ister ekrana yazdırır ister farklı yerlerde kullanabiliriz
# ayrıca return un fonksiyonu kırma kendisinden sonraki kodların okunmamasını sağlaması ile
# koşulların oluşmasıyla diğer işlevleri etkisiz hale getirebiliriz

def kup(sayi):
    return sayi * sayi

print(f'20 sayısının karekökü {kup(20)} idir.') # 20 sayısının karekökü 400 idir.

