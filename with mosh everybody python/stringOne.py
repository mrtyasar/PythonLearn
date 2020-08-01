# tek tırnak, çift tırnak, üç tırnak içine aldığımız her şey strgins olarak geçer
course = 'selamlar'
print(type(course))

courseOne = "evet merhabalar"
print(type(courseOne))

# üç tırnağı birden fazla satırlık bir işimizi olduğunda kullanırız
courseTwo = """
Hi john,

Here is our first email to you.

THank you,
The support team.
"""
print(courseTwo)
print(type(courseTwo))

# eğer karakter dizimizde ' tek tırnak işaretini kullanacaksak
# çift tırnak işaretiyle oluşturmamız lazım

# eğer karakter dizimizde " çift tırnak işaretini kullanacaksak
# tek tırnak işareiyle oluşturmamız lazım

# fakat karakter dizimizde hem ' tek tırnak hemde " çift tırnak işaretini kullancaksak
# üç tırnak işaretiyle oluşturmamız lazım

print('çift "tırnak" işareti kullandık.')
print("tek 'tırnak' işareti kullandık.")
print(""" hem 'tek tırnak' işaretini kullandık hemde "çift tırnak" işaretini kullandık. """)

# karakter dizilerinde indeks numaralarına göre elemanları almak

kurs = 'Python for begginers'

print(kurs[0]) # ilk eleman P
# sondaki elemanları almak için - den faydalanırız
print(kurs[-1]) # s
print(kurs[-2]) # r

# dilimleme
# belli aralık vererek elemanları toplamak

print(kurs[0:3])
# bir sayıdan bir sayıya gideceksek gideceğimiz sayının bir üstü sayısını yazmamız gerekir


# 0 dan başlayacaksak 0 yazmamıza
# bir sayıdan en son elemana kadar alacaksak en sondaki indeksi yazmamıza gerek yoktur
print(kurs[:3])
print(kurs[3:])

print(kurs[:]) # tüm stringi aldık
print(kurs[0:])


# egzersiz

name = 'Jennifer'
print(name[1:-1])