#----------------------------------#
######### ARİTMETİK İŞLEÇLER #######
#----------------------------------#

# +   toplama
# -   çıkarma
# *   çarpma 
# /   bölme
# **  kuvvet
# %   modülüs/kalan bulma
# //  taban bölme/ tam bölme

#aritmetik işleçler sayısal işlemler yapmamızı sağlar

print(45+57)#102

#yalnız + ve * işaretleri karakter dizileri içinde kullanılabilir
#karakter dizilerini birleştirmek için + işareti
print("Selam "+"Bugün "+"Hava çok güzel.")#Selam Bugün Hava çok güzel.
# * işareti karakter dizileri tekrarlamak için kullanılabilir
print("w"*3+".tnbc1"+".com")#www.tnbc1.com

# % işleci sayının bölümünden kalanı bulur
print(30 % 4)#2
#sayının kalanını bularak tek mi çift mi olduğunu bulabiliriz
sayi = int(input("Bir sayı giriniz: "))
if sayi % 2 == 0:
    print("Girdiğiniz sayı bir çift sayıdır.")
else:
    print("Girdiğiniz sayı bir tek sayıdır.")
#eğer bir sayının 2 ye bölümünden kalan 0 ise o sayı çift bir sayıdır

#veya bu % işleci ile sayının başka bir sayı ile tam bölünüp bölünmediğini
# bulabiliriz

print(36 % 9)#0 #yani 36 9 a tam bölünüyor
#program yazalım:
bolunen = int(input("Herhangi bir sayı giriniz: "))
bolen = int(input("Herhangi bir sayı daha giriniz: "))

sablon = "{} sayısı {} sayısına tam".format(bolunen,bolen)
if bolunen % bolen == 0:
    print(sablon,"bölünüyor!")
else:
    print(sablon,"bölünmüyor!")    
#çıktı:
#Herhangi bir sayı giriniz: 2876
#Herhangi bir sayı daha giriniz: 123
#2876 sayısı 123 sayısına tam bölünmüyor!

# bir sayının son basamağını elde etmek içinde kullanabiliriz
#bu yüzden bir sayının 10 bölümünde kalanını buluruz
print(65 % 10)#5
print(543 % 10)#3

#----------------#
#--//-tam bölme--#
#----------------#

a = 6 / 3
print(type(a))#float # 2.0
#pythonda sayıların bölmelerin sonucu kesirli olur yani float tipinde
b = 6 // 3
print(b)#3
print(type(b))#int #tam bölebildik

print(int(a))#2 # bu şekilde de float tipini inte çevirebildik

#----------------#
#     ROUND      #
#----------------#

#round() bir gömülü fonksiyondur
#bu fonksiyonun bir sayının değerini yuvarlamamızı sağlar

print(round(2.70))#3
print(round(2.30))#2

print(round(5.68,1))#5.7
print(round(5.68,2))#5.68
print(round(7.9,2))#7.9

#-----------------#
#        **       #
#-----------------#

#bir sayının karesini bulmak 
#bunun için 2 rakamına ihityacımız vardır
print(124**2)#15376

#bir sayının karakökünü bulmak
#karakökünü bulmak için 0.5 e ihtiyacımız vardır

print(625 ** 0.5)#25.0
#eğer ondalıklı sayı yani float tipli sayı istemiyorsak
#ifadeyi işlemi int tipine çevirmemiz gerekir
print(int(625 ** 0.5))#25

#bir sayının küpünü bulmak
#küpünü bulmak için 3 rakamına ihtiyacımız vardır

print(124 ** 3)#1906624

#bu işlemleri pow() fonksiyonları ile de yapabiliriz
print(pow(24,3))#13824
print(pow(96,2))#9216


#-------------------------------------#
#      KARŞILAŞTIRMA İŞLEÇLERİ        #
#-------------------------------------#

#işlenenler arasında bir karşılaştırma ilişkisi kuran işleçlerdir

# ==   eşittir
# !=   eşit değildir
# >    büyüktür
# <    küçüktür
# >=   büyük eşittir
# <=   küçük eşittir

parola = "xyz05"
soru = input("parolanız: ")
if soru == parola:
    print("doğru parola!")
elif soru != parola:
    print("yanlış parola!")

#başka bir örnek:
sayi = input("sayı: ")
if int(sayi) <= 100:
    print("sayı 100 veya 100'den küçük")
elif int(sayi) >= 100:
    print("sayı 100 veya 100'den büyük")


#-------------------------#
#      BOOL İŞLEÇLERİ     #
#-------------------------#

#bool da sadece iki değer vardır true ve false
#bilgisayar biliminde olduğu gibi 0 false dir 1 true dur

a = 1
print(a == 1)#a değeri 1 e eşit midir?
#True

print(a == 2)#False

# o değeri ve boş veri tipleri False'Dir
# bunun haricinde kalan her şey True
#bu durumu bool() adlı fonksiyondan yararlanarak öğrenebiliriz
print(bool(4))#True
print(bool("armut"))#True
print(bool(" "))#True
print(bool(2288281))#True
print(bool("0"))#True
print(bool(0))#False
print(bool(""))#False

#bool değerleri yazılım dünyasında önemli bir yeri vardır
#daha önce kullandığım koşul bloglarında koşulun gerçekleşmesi
#veya gerçekleşmemesi bool a bağlıdır yan, true ve false

isim = input("isminiz: ")

if isim == "Ferhat":
    print("Ne güzel bir isminiz vardır")
else:
    print(isim,"ismini pek sevmem!")

#isminiz: caner
#caner ismini pek sevmem!

# eğer diyoruz isim ferhat ifadesi true ise şunu göster diyoruz
# eğer true değeri dışında herhangi bir şey yani false ise şunu göster diyoruz

isim = input("isminiz: ")
print(isim == "Ferhat")#True

#
b = ""
print(bool(b))#False

#içi boş veri tiplerin her zaman false olacağını bilerek şöyle 
#program yazabiliriz:

kullanici = input("Kullanıcı adınız: ")
if bool(kullanici) == True:
    print("Teşekkürler")
else:
    print("Kullanıcı adı alanı boş bırakılamaz!")

# eğer kullancı bir şeyler yazarsa bool(kullanici) komutu true verecek
# ekrana teşekkürler yazısı yazılacak
# eğer kullanıcı bir şey yazmadan entera tıklar ise false olacak ve else çalışacaktır

#bu işlemi genellikle şu şekilde yazarız:
kullaniciOne = input("Kullanıcı adınızı yazınız: ")
if kullaniciOne:
    print("Teşekkürler")
else:
    print("kullanıcı adı boş bırakılamaz")   

#---------------------------------#

#        BOOL İŞLEÇLERİ           # 

#---------------------------------#

#AND
#OR
#NOT

#and
#gmail giriş sistemi yazalım
#gmail giriş sisteminde kullanıcı adı ve parola yani her ikisi de doğru olmalıdır

kullaniciAdi = input("Kullanıcı adınız: ")
parola = input("Parolanınız: ")

if kullaniciAdi == "AliVeli":
    if parola == "123456":
        print("Sisteme hoşgeldiniz")
    else :
        print("Yanlış kullanıcı adı veya parola!")
else:
    print("Yanlış kullanıcı adı veya parola")


#bu işlemi daha kolay yazabiliriz

kullanici = input("Kullanıcı adınızı yazınız: ")
sifre = input("şifrenizi yazınız: ")

if kullanici == "aliveli" and sifre == "12345":
    print("programa hoşgeldiniz")
else:
    print("Yanlış kullanıcı adı veya parola")

#and işlecini kullanarak iki durumu bağladık
#and işlecinin mantığı her iki durumun gerçekleşmesidir
#bütün koşullar gerçekleşiyorsa true döner
#onun haricinde tüm sonuçlar false dir

a = 23
b = 10
print(a == 23)#True
print(b == 10)#True

print(a == 23 and b == 10)#True

print(a == 23 and b == 15)#False

# OR
#or veya demektir
#her iki koşuldan biri true olursa yine de çalışır

c = 10
d = 100
print(c == 10)#True
print(d == 100)#True

print(c == 1 or d == 100)#True
# c koşulu yanlış olsa da d koşulu doğru olduğu için çıktı True oldu

# sınavdan alınan notların harf karşılığını gösteren program
x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")
elif x >= 90 and x <= 100:
    print("A aldınız")
elif x >= 80 and x <= 89:
    print("B aldınız.")
elif x >= 70 and x <= 79:
    print("C aldınız")
elif x >=60 and x <= 69:
    print("D aldınız.")
elif x >= 0 and x <= 59:
    print("F aldınız.")

#şu şekilde daha kısa biçimde yazabiliriz

z = int(input("notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yoktur.")
elif z >= 90 <= 100:
    print("A aldınız")
elif z >=80 <= 89:
    print("B aldınız")
elif z >= 70 <= 79:
    print("C aldınız")
elif z >= 60 <=69:
    print("D aldınız")
elif z >=0 <=59:
    print("F aldınız")

# and i kaldırdığımızda aynı sonucu alabiliyoruz

## not ##

# not bir bool işlecidir. türkçe karşılığı değil demektir
# özellikle kullanıcı tarafından değer girilip girilmediğini 
#denetlmek için kullanılır

#eğer kullanıcı değer girilise not değeri çalışacak
#eğer kullanıcı boş bırakılsa true değeri çalışacak

parola = input("Şifrenizi giriniz Lütfen: ")
if not parola:
    print("Şifre boş bırakılamaz")

#şifrenizi giriniz yazısı geldiğinizde cevap vermeyip entera tıkladım
#değer true olunca print fonksiyonu çalıştı

print(bool(parola))#false
#makineye şunu soruyoruz aslında:
#parola boş bırakılmamış değil mi?
#makinede bize: hayır boş bırakılmış diyor

print(bool(not parola))#True
#makineye parola boş bırakılmış değil mi? sorusunu soruyoruz
#makine de bize true evet boş bırakılmış diyor

#yani ikisinin arasındaki fark bırakılmamış/bırakılmış değil? midir

#yani not isleçi makineye "boş bırakılmış değil mi?" sorusunu soruyor
#eğer boş bırakıldıysa cevap True oluyor evet bırakılmış demek oluyor

#----------------------------------#

#      Değer Atama İşleçleri       #

#----------------------------------#

# değer atama işlemi "=" işleciyle yapılır
a = 25
#a değişkenin içine 25 değerini atadık

## += işleci
#değişkenin değerine değer eklemek için kullanılır
a += 10 # a değişkenin değerine 10 değeri daha ekledik
print(a) # 35

## -=
#değişkenin değerinin düşürmek yani çıkarmak için kullanılır
a -= 5 #a değişkeninden 5 değer çıkardık
print(a)#30

## /= 
# değişkenin değeriyle bölme işlemi yapmak için kullanılır
a /= 2 #a değişkenin değerini 2 sayısıyla böldük
print(a)#15.0

## *=
#değişkenin değerini çarpmak için kullanılır
a *= 4 # a değişkenin değerini 4 ile çarptık
print(a)#60.0

## %=
#değişkenin değerinin bölme işleminde kalanını bulmak için kullanılır
a %= 7 #a değişkenin değerinin 7 ile bölünmesinden kalanını bulduk
print(a)#4.0

## **=
#değişkenin değerinin kuvvetini, küpünü ve karakökünü bulmak için kullanılır
a **= 2#a değişkenin kuvvetini bulduk
print(a)#16.0

## //=
#değişkenin değerinin tam bölünmesini bulmak için kullanılır
a //= 2
print(a)#8

#bu işleçler normalde şu işlemi yapar örneğin
#a = a + 5
#print(a)#5
#fakat bu işlem hızlı bir seçenek değildir ama mantıksal olarak bu şekilde işlem yapar

#işleçlerin sağ ve solda olma farkı
# += veya =+  -= veya =-

a =- 5
print(a) # -5
# a değerine -5 değerini verdik

## := (walrus operatörü)
#örnek:
giris = len(input("Adın ne?"))

if giris < 4:
    print("Adın kısaymış")
elif giris < 6:
    print("Adın biraz uzunmuş")
else:
    print("Uzun bir adın varmış.")

#bu kodu := işlecini kullanarakta yazabiliriz

if (giris := len(input("Adınız nedir?"))) < 4:
    print("Adın kısaymış")
elif giris < 6:
    print("Adın biraz uzunmuş")
else:
    print("Çok uzun bir adın varmış.")

# := tek avantajı işlemimizi tek satıra sığdırması
# çok kullanılmaz
#zaten yeni bir işleç olduğundan sadece python 3.8.1 de çalışır

#--------------------------------#
#       AİTLİK İŞLEÇLERİ         #
#--------------------------------#

#bir karakter dizisinin değişkenin içinde bulunup bulunmadığını
#kontrol edebilmemizi sağlar
#bu işlemi in adlı işleç sayesinde yaparız

a = "asdfg"
print("a" in a)#True
#makineye "a" değeri a değişkenin içinde var mı? sorruyoruz
print("A" in a)#False
print("j" in a)#False
# "j" değeri a değişkenin içinde var mı? cevap: Hayır yok False


#--------------------------------#
#        KİMLİK İŞLEÇLERİ        #
#--------------------------------#

#pythonda her şeyin yani her nesnenin arka planda bir kimlik numarası vardır
#bunu öğrenmek için id() adlı fonskiyondan yararlanırız

a = 50
print(id(a))#140705130925248
# a nın kimlik numarasını yazdır dedik

name = "Hello my name is Murat"
print(id(name))#2704421625648

#pythonda her nesenin eşsiz tek ve benzersiz bir kimlikleri vardır

#python belli bir değere kadar önbellekte aynı kimlik numarasıyla tutar

nameOr = 100
print(id(nameOr))#140705130926848

nameOrOne = 100
print(id(nameOrOne))#140705130926848

#belli bir değeri artan değerleri önbellekte farklı kimlik no larıyla tutar
y = 1000
print(id(y))#2467428862544

u = 1000
print(id(u))#1586531830352

#aynı değere sahip olarak gözükselerde python farklı kimlikle tanıtıyor

#bunun nedeni python sadece ufak nesneleri önbellekte tutar
#diğer büyük nesneleri ise yeni bir depolama işlemi yapar
#ufak ve büyük değerleri öğrenmek için:

for k in range(-1000,1000):
    for v in range(-1000,1000):
        if k is v:
            print(k)
#çıkan sonuca göre -5 ila 256 arasındaki değerleri önbellekte tutabiliyor

## is

number = 1000
numberOne = 1000
print(id(number))#2209573079632
print(id(numberOne))#2756858382928

print(number is 1000)#False
print(numberOne is 1000)#False

#is kimlikliklerine göre eşit midir aynı mıdır sorusunu sorar

#is ve == işleci çok kere karıştılır ikisinin arasındaki fark:
#is nesnelerin kimliklerine bakarak aynı mı olduklarını inceler
# == ise nesnelerin değerlerine bakarak aynı mı olduklarını inceler

print(number is 1000)#false
#ayrı kimlikleri olduklarından cevap false
print(number == 1000)#True
#a 1000 değerine sahip oldukları için cevap true
#is in arka planda yaptığı şey kabaca bu:
print(id(number)==id(1000))#false

ornek = "Python"
print(ornek is "Python") #True

ornekOne = "Python güçlü ve kolay bir proglama dilidir"
print(ornekOne is "Python güçlü ve kolay bir proglama dilidir")#False

print(ornekOne == "Python güçlü ve kolay bir proglama dilidir")#True

#sayısal değerlerde olduğu gibi karakter dizilerinde de küçük olanlar önbellekte
#büyük olan karakter dizileri içinde yeni bir kimlik ve depolama tanınmaktadır



##  UYGULAMA ÖRNEKLERİ  ##

#------------------------------------#
#    BASİT BİR HESAP MAKİNESİ        #
#------------------------------------#

#programımız bir hesap makinesi olacak
#kullanıya bir sayı girecek ve bu sayı ile topla mı çıkarma mı yapacak karar verecek
#buna göre ise işlemler yapacak

#kullanıcıya bazı seçenekler sunalım:
giris = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karakökünü hesapla
"""
print(giris)
soru = input("Yapmak istediğiniz işlemin numarasını giriniz: ")#kullanıcan hangi işlemi yapacağını soracağız
if soru == "1":
    sayi1 = int(input("Toplama işlemi için ilk sayıyı giriniz: "))
    sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
    print(sayi1,"+",sayi2,"=",sayi1+sayi2)      
elif soru == "2":
    sayi3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
    sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
    print(sayi3,"-",sayi4,"=",sayi3-sayi4)    
elif soru == "3":
    sayi5 = int(input("Çarpma işlemi için ilk sayıyı giriniz: "))
    sayi6 = int(input("Çarpma işlemi için ikinci sayıyı giriniz:"))
    print(sayi5,"*",sayi6,"=",sayi5*sayi6)
elif soru == "4":
    sayi7 = int(input("Bölme işlemi için ilk sayıyı giriniz: "))
    sayi8 = int(input("Bölme işlemi için ikinci sayıyı giriniz: "))
    print(sayi7,"/",sayi8,"=",sayi7/sayi8)
elif soru == "5":
    sayi9 = int(input("Karesini hesaplamak istediğiniz bir sayıyı giriniz: "))
    print(sayi9,"sayının karesi =",sayi9 ** 2)
elif soru == "6":
    sayi10 = int(input("Karekökünü hesaplamak için istediğiniz sayıyı giriniz: "))
    print(sayi10,"sayısının karakökü =",sayi10 ** 0.5)
else:
    print("Yanlış giriş.")
    print("Aşağıdaki seçeneklerden birini giriniz: ",giris)

"""
Temel olarak program şu şekilde:

eğer böyle bir durum varsa:
    şöyle bir işlem yap
yok eğer şöyle bir durum varsa:    
     böyle bir işlem yap
eğer bambaşka bir durum varsa:
     şöyle bir şey yap
"""

#-----------------------------------#
#  SÜRÜME GÖRE İŞLEM YAPAN PROGRAM
#-----------------------------------#

#Pythonda 3.x serisinde yazılan kodlar 2.x serinde çalışmaz
#yazdığımız kodların hangi python sürümünde çalıştırılmasını isteyebilirz
#veya 3.x de yazdığımız kodların 2.x çalıştırılması haline kullanıya hata mesajı verdilebiliriz

#sys modulünü çağıralım içe aktaralım
import sys
#modül içindeki istediğimiz değişkene erişelim
print(sys.version_info)
#sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)
#birde version değişkenin vereceği çıktıya bakalım
print(sys.version)#3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
#fakat işimize version_info değişkeni yarıyor
#version_info nun verdiği çıktı gözüken bazı şeyler:

#major, python serisinin ana sürüm numarası
#minor, alt sürüm numarası
#micro, en alt sürüm numarasını verir

#bu değerlere ulaşmak için:
print(sys.version_info.major)#3
print(sys.version_info.minor)#7
print(sys.version_info.micro)#4

#Programımızı hangi sürüm ile çalıştırılması gerektiğini kontrol eden bir program yazalım
#bu program için major ve minor u kullanacağız ihtiyaç dahilinde micro da kullanabiliriz
import sys

_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
_3x_metni = "Programa Hoşgeldiniz!"

if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)

#burada ilk başta modül içindeki araçları kullanmak için import ediyoruz
#daha sonra 2.x serisini kullanan biri için hata mesajı oluşturuyoruz
#değişkenlerin adları sayıyla başlayamayacağı için alt çizgi ile başladık
#sonra python3 kullanıcıları için merhaba metni yarattık
#eğer dedik major numarası yani ana sürümü 3 ten küçükse şunu yazdır
#bunun dışındaki bütün durumları için ise _3x_metnini bastır dedik

# 2.x sürümlerinde türkçe karakterleri makine algılayamıyordu
#bunu çözmek için ise :
# -*- coding: utf-8 -*- 
#bu kodu yapıştırıyorduk 3.x te bu sorun kalkmıştı
#fakat bu sadece programın çökmesini engeller türkçe karakterler bozuk gözükür
#örneğin _2x_metin 2.x sürümlerinde çalışınca şöyle gözükür:
"""
Python'Ä±n 2.x sÃ¼rÃ¼mlerinden birini kullanÄ±yorsunuz.
ProgramÄ± Ã§alÄ±ÅŸtÄ±rabilmek iÃ§in sisteminizde Python'Ä±n
3.x sÃ¼rÃ¼mlerinden biri kurulu olmalÄ±."""

#bunu engellemek için karakter dizimizin önüne u eklemek
# u ise unicode kavramından gelmektedir
_2x_metni = u"""
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
#3 ten küçük sürümlere hata mesajı yazdırabildik
#şimdi ise 3.4 gibi küçük sürümlere hata mesajı yazdırabiliriz
hataMesaj3 = u"""
Şuan Python'un eski sürümünü kullanıyorsunuz. 
Lütfen güncelleyiniz!
"""
if sys.version_info.major == 3 and sys.version_info.minor == 8:
    print("bla bla")
else:
    print(hataMesaj3)

#böylece 3.8 altı kullanan kullancılara bir heta mesajı gösterdik

#bu işlemi için version değişkenini de kullanabiliriz
if "3.7" in sys.version:
    print("Güncel versiyondasınız")
else:
    print(hataMesaj3)







