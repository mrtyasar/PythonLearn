"""
Ters Taksim (\)
"""
#print("Selamlar "Bugün"yaşamak lazım") #syntaxError: invalid syntax
#hata aldık çünkü python karakter dizisinin nerede sonlandığını anlayamadı

#bunu şu şekilde yazarak hata almayabiliriz

print('Selamlar "Bugün" yaşamak lazım') #Selamlar "Bugün" yaşamak lazım

#tırnak işaretlerini değiştirmeden ve hata alamadan yazmak için
# ters taksimden yararlanırız

print("Selamlar \"Bugün\"yaşamak lazım")#Selamlar "Bugün" Yaşamak lazım

print("\"Book\"kelimesi Türkçede\"kitap\"anlamına gelir.")
# "Book" kelimesi "Kitap anlamına gelir"

#normalde pytonun affallaması ve hata vermesi gerekir
#fakat ters taksim(\) işareti sayesinde hatadan kaçabiliyoruz

# \ işareti ve buna benzer işaretler Pythonda kaçış dizisi(escape sequence) denir
# kaçış dizileri, karakter dizilerini tanımlarken oluşabilecek hatalardan kaçmamızı sağlar
#örnek:

print("hava güzel \"cicekler\" daha güzel")
#pythonda işlemler soldan sağa doğru ilerler
#pythonda karakter dizesi tanımlamak için tırnak işaretlerinden yararlanırız
#makine çift tırnağı görüp bunu string olduğunu anlıyor fakat sonra son işaretine kadar karar veremiyor
#çift tırnakla başladığımız stringde ilerleyince bir tane daha karşılaşıyor bunun son olduğunu düşünüyor
#fakat bir tane dahayla karşılaşınca kafası karışıp hata veriyor
#hata verme yolu budur

#bu hatayı almamak için ise tırnak içinde tırnak işareti oluşturduğumuz şeyin önüne \ koyuyoruz
#bu dmeektir ki aradığın işaret bu değildir sen karakter dizisini okumaya devam et
#sonra diğer çift tırnağın önüne \ koyarak aynı mesajı makineye iletmiş oluyoruz 
#ve bu işaretleri atlayarak son tırnak işaretini bularak işlemini hatasız sonlandırıyor

#ters taksimi üç tırnak işaretinin yerine kullanabiliriz
#etkileşim kabuğunda """ tırnakla paragraf yazabilir ve her enter a bastğımızda
# makine bize ... yani yazmaya devam et diyordu bu işlemi ters taksimle yapabiliriz

print("Selam arkadaşlar Bugün kod yazdım\
    kod yazmayı çok severim.\
        kod yazmak benim için sanattır.")

  #tert taksimi kullanmasaydık program bize hata verirdi

"""
Satır Başı (\n)
"""
#\n işareti yeni bir satıra geçmemizi sağlar
print("birinci satır\nikinci satır\nüçüncü satır")
#birinci satır
#ikinci satır
#üçüncü satır

baslik = "Türkiye'de Özgür Yazılımın Geçmişi"
print(baslik,"\n","-"*len(baslik),sep="")
#Türkiye'de Özgür Yazılımın Geçmişi
#----------------------------------

baslikOne = "Python Proglama Dili"
print(baslikOne,"\n","-"*len(baslikOne),sep="")
#Python Proglama Dili
#--------------------

baslikTwo = "Alişveriş Listesi"
print(baslikTwo,"\n","-"*len(baslikTwo),sep="")
#Alişveriş Listesi
#-----------------

#burada ne yapıyoruz
#baslikTwo değişkenin içine "Alişveriş Listesi" dizisini atıyoruz
#print fonskiyonu sayesinde değişkenin değerini ekrana yazdırıyoruz
#kaçış dizimiz \n sayesinde bir alt satıra geçiyoruz
# alt satırda - işaretini baslikTwo 'nun içindeki eleman sayısı kadar çarpıyoruz
#bu sayede alttaki işaretler eleman sayısıyla bir olacak ve düzgün gözükecek
#daha sonra sep in içindeki boşluk yerine boş bir karakter içeren dizi ekliyoruz

# \n işaretini kullanmasaydık ne olurdu
print(baslikTwo,"-"*len(baslikTwo),sep="")
#Alişveriş Listesi-----------------
#bir alt satıra geçmeyerek çizgileri yanına dizdi

#len fonskiyonunu neden kullandık
#değerimizin altına ona eşit çizgi eklemek istedik
#çizgileri değişkenin içindeki değerin eleman sayısına çarparak eşit şekilde çizginin eklenmesini sağladık
#bu sayede daha düzgün bir görüntü elde ettik

#sep parametresinin öntanımlı değerini neden sildik
#sep parametresinin öntanımlı değeri boşluktur

print(baslikTwo,"\n","-"*len(baslikTwo))

#Alişveriş Listesi
# -----------------
#çizgilerin sağa kaydığını farkettik
#bunun nedeni sep parametresi çizgilerin başına boşluk koydu
#bunu istemediğimiz için boşluk karakteri yerini boş bir karakter dizisi yerleştirdik ("")

#karakter dizinlerin içinde kaçış dizilerini gözden kaçırırsak python bize hata verebilir
#mesala "C:" dizindeki nisan adlı klasörün masraflar.txt dosyasına ulaşmak istiyelim

print("C:\nisan\masraflar.txt")
#uzaktan görününce doğru gözüküyor
# \n adlı kaçış dizisi yüzünden \n sonrası bir alt satıra yazdırılıyor
#C:
#isan\masraflar.txt

#bu yüzden \ bu işarete ve bundan sonra gelen işaretlere çok dikkat etmek gerekir

#bir hata almasakta open fonksiyonuyla masraflar.txt i açmaya çalışırsak programımız hata alır çöker

#open("C:\nisan\masraflar.txt") #hata aldık
#OSError: [Errno 22] Invalid argument: 'C:\nisan\\masraflar.txt'

#bu sorunu çözmek için
#ters taksim işaretini çiftlemek sorunu çözer
#tutarlılık için tümünü bu şekilde yapmak daha mantıklıdır

#open("C:\\nisan\\masraflar.txt")

#ters taksim yerine düz taksimde kullanabiliriz

#open("C:/nisan/masraflar.txt")

#sorunumuz çözüldü

"""
Sekme(\t)
"""

#sekme işareti parametreler arasında belli bir boşluk bırakmak istediğimizde kullanırız

print("abc\tdfgh")#abc     dfgh

print("bir","iki","üç",sep="\t")#bir     iki     üç

print(*"12345678",sep="\t")
#1       2       3       4       5       6       7       8

#her zaman ki kaçış dizilerine dikkat etmemiz laızm 
#gözümüzden kaçabilir ve programımız hata verebilir: örneğin:
#open("C:\nisan\masraflar\toplamMasraf.txt")
#hata aldık çünkü makine \toplamMaraf.txt i değil \t olarak algıladı

#sorunu ise \n de çözdüğümüz gibi
#ya ters taksimleri çiftlicez ya da düz taksim kullancak
#open("C:\\nisan\\masraflar\\toplamMasraf.txt")
#open("C:/nisan/masraflar/toplamMasraf.txt")

"""
Zil Sesi(\a)
"""
print("\a") #!bip!

# \a zil sesi üretilmesini sağlar
# istersek bu sesi çoğaltabiliriz
print("\a"*10)

#bu kaçış dizisi linuxta nadiren windowsta ise bazen çalışır
#yani çalışıp çalışmadığından emin olamayız

"""
Aynı Satır Başı(\r)
"""

print("Murat\rCan")#Canat
print("selmalar bugün\rdünyadayız")

print("1234\r456")#4564

#bu kaçış dizisi aynı satırın en başına dönülmesini sağlar
#normalde pythonda işlemler soldan sağa doğru işlenir

#fakat kaçış dizisi \r yi kullanırsak şu işlem gerçekleşir
# \r kaçış dizisinden sonra gelen karakterler satır başındaki karakterlerin
#üzerine yazacaktır

print("merhaba\rDünya")#Dünyaba
# \r den sonrası olan Dünya en başa dönüp merhaba nın üzerine yazıldı
#merhabadan alttan kaan ba da dünya kelimesine eklenerek Dünyaba oldu

print("123346\r456")#456346
#456, 123346 ın üzerin yazıldı ve artan 346 karakter dizileri 456 ın yanına eklendi

"""
Düşey Sekme (\v)
"""
print("düşey\vsekme")
#düşeysekme
#     sekme
#bu kaçış dizisi her yerde çalışmaz çalışırsa da bunun gibi yanlış şekilde çalışır
#birden fazşa platform şeklinde çalışmak üzere tasarlanan programlarda kullanılması önerilmez

"""
İmleç Kaydırma(\b)
"""

print("selamlar\bmesala")
#bir sola kaydırarak sonuç: selamlamesala

print("çanakkale\bgeçilmez")#çanakkalgeçilmez

#print otomatik olarak parametreler arasında boşluk bırakır 
# \b ile bir sola kaydırarak boşluğu ortadan kaldırabilir

print("istihza","\b","\b.com")
#istihza.com

print("selam","\b","\b,arkadaşlar")#selam,arkadaşlar

#küçük Unicode (\u)

print("\u0130")#İ

print("\u9892")#颒

print("\u0987")#ই

#UNICODE karakterlerin harflerin sayıların ve bilgisayar ekranında gördüğümüz
#öteki bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir
#bu sistemde kod konumu(code point) adı verilen bu numaralar
#özel bir şekilde gösterilir

#büyük Unicode(\U)

#küçük unicode gösterim
print("\u0131")#ı

print("\U00000131")#ı

#büyük unicodenin tek farkı küçük unicode den daha fazla sayıdan oluşması
#yoksa ikiside aynıdır

#Uzun Ad (\N)

#UNICODE sistemi ilgili başka bir kaçış dizisidir

#UNICODE sisteminde her karakterin tek ve benzersiz bir kod konumu olduğu gibi
#tek ve benzersiz uzun adı da vardır

#örneğin UNICODE sisteminde a harfinin uzun adı şöyledir:
#LATIN SMALL LETTER A

#bir karakterin unicode sistemindeki uzun adını öğrenmek için:

import unicodedata
print(unicodedata.name("ş"))
#LATIN SMALL LETTER S WİTH CEDİLLA
print(unicodedata.name("r"))
#LATIN SMALL LETTER R

#unicodedata da os,sys ve keyword gibi modüldür
#name adlı fonskiyonu kullanarak parantez içinde belirttiğimiz her karakterin
#unicode sistemindeki uzun adını elde etmiş oluruz

# \N kaçış dizisi ise bu uzun isimleri programda kullanabilmemizi sağlar
#bu kaçış dizisi sayesinde uzun adları ile birlikte kullanarak asıl karakterleri elde ederiz

print("\N{LATIN SMALL LETTER A}")#a
print("\N{LATIN SMALL LETTER U}")#u
print("\N{LATIN CAPITAL LETTER S WITH CEDILLA}")#Ş

#\u,\U ve \N kaçış dizileri UNICODE sistemi ile ilgili çalışmalar yapmak isteyenler için
#faydal araçlardır


#Onaltılı Karakter(\x)

# \x kaçış dizisini kullanarak onaltılı(hexadecimal) sayma sistemindeki bir sayının
#karakter karşılığını gösterebilirsiniz

print("\x41")#A

#on altılı sayma sisteminde 41 sayısı A harfine karşılık geliyormuş
#http://www.ascii.cl/ sitesinde hex sütunu altında gösterilenler on altılık sayılardır
#bu sayıların karşılığı ise symbol sütununda yazar

print("\x4E")#N
print("\x2E")# .
print("\x54")#T

#Etkisizleştirme(r)

print("Kurulum dizini: C:\aylar\nisan\toplammasraf")
#Kurulum dizini: C:ylar
#isan    oplammasraf

#python \a karakterini görünce bip sesi veriyor
#\n karakterini görünce bir alt satıra geçiyor
#\t karakterini görünce ise tab tuşuna basılmış gibi boşluk bırakıyor

#bunun olmasını engellemek için ters taksimleri çiftleyebiliriz
#fakat bunun daha kolay bir yolu vardır
print(r"Kurulum dizini: C:\aylar\nisan\toplammasraf")
#Kurulum dizini: C:\aylar\nisan\toplammasraf

print("Kaçış Dizileri: \,\n,\t,\a,\\,r")
#Kaçış Dizileri: \,
#,       ,,\,r

print(r"Kaçış Dizileri: \,\n,\a,\\,r")
#Kaçış Dizileri: \,\n,\a,\\,r

# karakter dizisinin başında getirdiğimiz r
#karakter dizisinin içindeki kaçış dizilerin işlevlerini yok ediyor

#dikkat

#print("Kaçış dizisi: \") #hata aldık
#SyntaxError: EOL while scanning string literal

#çünkü \ işareti karakter dizisinin kapatan tırnak işaretini görmezden gelmesini sağlıyor
#bu yüzden ise kapanış tırnağını hiç yazmamışız gibi bir sonuç çıkıyor

#bu durumu r kaçış dizisi de engelleyemez

#bu durumu çözmek için ise kaçış dizisinin yanına boşluk bırakabiliriz
print("Kaçış Dizisi: \ ")
#Kaçış Dizisi: \
#veya da ters taksimleri çiftleyebiliriz


#Sayfa Başı(\f)

f = open("denemeOne.txt","w")
print("deneme\fdeneme",file=f)
f.close()

#denemeOne.txt i word la açınca deneme karakterlerini iki farklı sayfada yazdırdı
#bu kaçış dizisi eskiden kullanılırdı şimdilerde çok kullanılmaz
#bu kaçış dizisinin amacı bir sayfanın sona erip yeni bir sayfanın başladığını göstermektir
#yani eski model yazıcılar bu karakteri gördükleri noktada mevcut sayfayı sona erdirip bir  yeni sayfaya geçer


#Kaçış Dizilerine Toplu Bakış

"""
'' = karakter dizisini tanımlamak ve içinde kullanabilmemizi sağlar
"" = karakter dizisini tanımlamak ve içinde kullanabilmemizi sağlar
\  = karakter dizisi içindeki tırnak işaretleri kullanmamızı sağlar
\n = yeni bir satıra geçmemizi sağlar
\t = karakterler arasında sekme boşluğu bırakmamızı sağlar
\u = unicode kod konumlarını gösterebilmemizi sağlar
\U = unicode kod konumlarını gösterebilmemizi sağlar
\N = karakterleri UNICODE adlarına göre kullanabilmemizi sağlar
\x = onaltılı sistemdeki bir sayının karakter karşılığını verir
\a = destekleyen sistemlerde hopörlerden bip sesi verdirir
\r = aynı satırın başına dönülmesini sağlar
\v = destekleyen sistemlerde düşey sekme oluşturulmasını sağlar
\b = imlecin soluna doğru kaydırılmasını sağlar
\f = yeni bir sayfaya geçilmesini sağlar
r  = karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar
"""















