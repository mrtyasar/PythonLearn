"""
İnput() fonskiyonu
"""
#input fonksiyonu sayesinde kullanıcıdan bilgi alabiliyoruz

isim = input("İsminiz nedir? ")
print("İsminiz:",isim,end="!\n")

#input fonksiyonu sayesinde kullanıcıya ismini sorup ismini alabildik
#yaşını sorup yaşını yazdıralım

age = input("Yaşınız Kaçtır? ")
print("Demek",age,"Yaşındasınız.")
print("Genç mi yoksa yaşlı mı olduğunuza karar veremedim.")

#kullanıcıdan dairenin çapını girmesini istiyoruz
cap = input("Dairenin çapı: ")
#kullanıcının verdiği çap bilgisini kullanarak
#yarıçapı hesaplayalım buradaki int() fonskiyonu değeri int e çevirdi
#bunun nedeni pythonda kullanıcıdan alınan her türlü değer stringdir
yarıcap = int(cap)/2
#pi sayımız ise sabittir
pi = 3.14159
#yukarıdaki bilgileri kullanarak dairenin alanını hesaplayalım
alan = pi * (yarıcap*yarıcap)
#hesapladığımız alanı yazdıralım
print("Çapı",cap,"cm olan dairenin alanı: ",alan,"cm2'dir")

#cap ı inte çevirmeden 2 ye bölseydik hata alırdık çünkü string ifadelerle
#matematiksel işlemler yapamayız

"""
#Tip Dönüşümleri
"""
#bir veri tipine sahip değeri başka bir veri tipine çevrilmesine tip dönüşümleri denir
#tip dönüşleri çoğunlukla input fonskiyonu barındıran değişkenlere uygulanır
#bunun nedeni kullanıcıdan bilgi aldığımız değerin ilk başta string olması
#string ifadeyle de matematiksel işlemler yapamayız

sayi = input("Lütfen bir sayı giriniz: ")
#girilen sayının karesini 2 farklı yolla alalım
print("Girdiğiniz sayının karesi: ", int(sayi)**2)#196
print("Girdiğiniz sayının karesi: ", pow(int(sayi),2))#196

#eğer int veri tipine çevirmeseydik TypeError hatası alacaktık

#kullanıcıdan herhangi bir veri aldığımıza bu veri bize string(karakter dizisi) olarak gelecektir

#kullanıcıdan herhangi bir veri girmesini istiyoruz
sayiOne = input("Herhangi bir veri giriniz")
#kullanıcın girdiği veriyi bir değişkene atıyoruz
tip = type(sayiOne)
#kullanıcın girdiği verinin tipini ekrana yazdıralım
print("Girdiğiniz verinin tipi: ",tip)#str

#elimizde bulunan değerlerin hangi veri tipine sahip olduğunu bilmek önemlidir

number = input("Herhangi bir sayi giriniz:")
numberOne = input("Herhangi bir sayi giriniz:")
#kullanıcıdan aldığımız iki değeri toplayalım
print(number,"+",numberOne,"=",number+numberOne)#5+5 = 56
#amacımız 5 ile 6 yı toplayıp 11 elde etmek fakat değer str olduğu için 
#değerleri toplamak yerine birleştirdi

#bu ve bunun gibi işlemlerde sorun yaşamamak için tip dönüştürücülerden yararlanırız

"""
İnt()
"""
#kullanıcıdan aldığımız her değer ilk olarak karakter dizisi olarak gelir
#şayet o değerle aritmetik değerler yapmaksa amacımız değeri inte çevirmemiz gerekir

karakterDizisi = "25"
sayiTwo = int(karakterDizisi)
print(sayiTwo)#25
print(type(sayiTwo))#int

#bir değeri int e çevireceksek o değerin sayısal bir değer olması gerekir
#mesala muz kelimesini int değerine çeviremeyiz ve program hata verir

veri = input("Lütfen bir sayı giriniz: ")
#input() fonksiyonundan gelen karakter dizisini sayıya dönüştürüyoruz
numberThree = int(veri)
print("Girdiğiniz sayının karesi: ",numberThree**2)
#yeni bir değişkene attık ki veri değerin int halini sürekli başka yerde
#kullanabilelim

v1 = input("Toplama işlemi için herhangi bir sayı giriniz:")
v2 = input("Toplama işlemi için herhangi bir sayı giriniz:")

numberFour = int(v1)#v1 adlı karakter dizisini sayıya dönüştürüyoruz
numberFive = int(v2) #v2 adlı karakter dizisini sayıya dönüştürüyoruz

print(numberFour,"+",numberFive,"=",numberFour+numberFive)#100+289=389

"""
str()
"""
#karakter dizisi olan sayısal değerleri int tipine çevirebildik
#bazı durumlarda ise tam tersi olarak sayısal değerleri int veri
#tipine çevirmemiz gerekebilir
#bu durumlar çoğunlukla sadece karakter dizisyle çalışan fonksiyonlara
#ihtiyaç duyduğumuzda olabiliyor
#mesala len() fonskiyonu
#bu fonskiyon sadece string değerlerle çalışabilir

#string değere dönüştürme

numberSix = 24
kardiz = str(numberSix)
print(kardiz)#24
print(type(kardiz))#str

#len fonksiyonu için çevirmek

#bir değerin eleman sayısını öğrenmek istiyoruz fakat değer sayısal bir değer
#bu değeri ölçmek için tip dönüştürücü str() fonksiyonundan yararlanırız

topluSayi = 2382838488484
topluSayiStr = str(topluSayi)
print(len(topluSayiStr))#13

#yukarıdaki işlemi tek satırda da yapabilirdik

print(len(str(19283744790287)))#14
#python fonksiyonu içten dışa olarak değerlendirir
#makine ilk başta girdiğimiz sayısal değeri stringe çeviriyor
#daha sonra len fonksiyonuyla eleman sayısını buluyor
#ve sonunda ise print sayesinde ekrana yazdırıyor

"""
#Float()
"""
#float() fonskiyonu sayesinde karakter dizilerini veye tam sayılı
#sayısa değerleri float veri tipine çevirebilir

a = 23
print(type(a))#int

b = float(a)
print(b)#23.0
print(type(b))#float

#sayı değerli karakter dizilerinde de yapabiliriz

c = "100"
print(type(c))#str
print(c)#100

d = float(c)
print(d)#100.0
print(type(d))#float

#float fonksiyonu sayesinde tam sayılı ifadeleri kayan noktalı sayıya dönüştürdük

"""
#complex()
"""
print(type(12+0j))#complex / karmaşık

h = 16
u = complex(h)
print(u)#16+0j
print(type(u))#complex

o = "17"
p = complex(o)
print(p)#17+0j
print(type(p))#complex

#TEKRAR

#int()
#sayı değerli karakter dizisini veya kayan noktalı sayıyı tamsayıya(integrer) çeviri

intOrnek = "93939"
print(type(intOrnek))#str
intOrnekTwo = int(intOrnek)
print(intOrnekTwo)#939339
print(type(intOrnekTwo))#int

#float()
#sayı değerli bir karakter dizisini veya tamsayıyı
#kayan noktalı sayıya(float) çeviri

floatOrnek = "34"
print(type(floatOrnek))#str
floatOrnekThree = float(floatOrnek)#floata çeviriyoruz
print(floatOrnekThree)#34.0

floatOrnekTwo = 34
print(floatOrnekTwo)#34
floatOrnekFour = float(floatOrnekTwo)#floata çevirdik
print(floatOrnekFour)#34.0
print(type(floatOrnekFour))#float

#str()
#bir tam sayıyı veya kayan noktalı sayıyı karakter dizisine
#yani strin e çeviri

stringOrnek = 2929
print(type(stringOrnek))#int
#string değerine çevirelim
stringOrnekOne = str(stringOrnek)
print(type(stringOrnekOne))#str

stringOrnekFloat = 29.8
print(type(stringOrnekFloat))#float
#string değerine çevirelim
stringOrnekTwo = str(stringOrnekFloat)
print(type(stringOrnekTwo))#str

#complex()
#herhangi bir sayıyı veya sayı değerli karakter dizisini complex e çevirir

complexInt = 3737
print(type(complexInt))#int
print(complexInt)#3737

complexOrnek = complex(complexInt)
print(complexOrnek)#3737+0j

#her tamsayıyı veya kayan noktalı sayıyı karakter dizisine çevirebiliriz
#fakat her karakter dizisini tam sayıya veya kayan noktalı sayıya çeviremeyiz

#örneğin 45 veya 45.8 i string değer yapabiliriz
#fakat muz değerini int veya float yapamayız çünkü sayısal bir değer değil

#ÖRNEK UYGULLAMA

#her bir ayın kaç gün çektiğini tanımlayalım
ocak = mart = mayis= temmuz = agustos = ekim = aralık = 31
nisan = haziran = eylul = kasim = 30
subat = 28

#doğalgazın vergiler dahil metreküo fiyatı
birimFiyat = 0.79

#kullanıcı ayda ne kadar doğalgaz tüketmiş?
aylikSarfiyat = input("Aylık doğalaz sarfiyatınızı metreküp olarak giriniz:")

#kullanıcı hangi aya ait faturasını öğrenmek istiyor
donem = input("""#Hangi aya ait faturayı hesaplamak istersiniz?
(#lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")

#yukarıdaki input() fonskiyonundan gelen veriyi
#pythonun anlayabileceği bir biçime dönüştürüyoruz
#ay = eval(donem)
#kullanıcının günlük doğalagaz sarfiyatı
#gunlukSarfiyat = int(aylikSarfiyat)/ay
#fatura tutarı
#fatura = birimFiyat*gunlukSarfiyat*ay

#ekrana yazdıralım
#print("günlük sarfiyatınız:  \t",gunlukSarfiyat,"metreküp\n",
#tahmini fatura tutarı: \t",fatura,"TL",sep="")

#---------------------------------------------

#### EVAL() VE exec() Fonkisyonu ########

print("""
Basit bir hesap makine uygulaması:
işleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra ENTER
tuşuna basın.)""")

veri = input("işleminiz: ")
hesap = eval(veri)

print(hesap)

#eval() fonksiyonun görevi kendisine verilen karakter dizilerini
#değerlendirmeye tabi tutmak ya da işlemektir

#yukarıdaki programı yorumlayalım:
#print fonksiyonuyla kullanım kullavuzuna benzer bir metin yerleştirdik
#ardından kullanıcıdan alacağımız değerleri veri adlı değişkene atadık
#sonra ise kullanıcıdan gelen veriyi eval() fonksiyonuyla değerlendirmeye tabi tutuyoruz
#yani kullanıcın girdiği komutları işleme sokuyoruz
#örneğin kullanıcı 46 / 2 gibi bir veri verdiyse
#eval fonskiyonuyla bu 46/2 yi işletiyoruz
#sonra bu işlemin sonucunu hesap adlı bir değişkene atıyoruz

#diyelim ki eval kullanmadan işlem yaptırmaya çalışalım
veriOne = input("İşleminiz: ")
print(veriOne)#10*20
#evali kullandığımız kodda 10*20 yazdığımızda 200 cevabını
#evali kullanmadığımız kodda ise 10*20 yazdığımıza 10*20 cevabını alıyoruz

#yani eval kullanıcın girdiği her veriyi python komutu olarak algılar ve
#bu veriyi işleme sokar yani 10*2* gördüğünde direk ekrana yzdırmak yerine
#işlemin sonucunu yazar

### eval() kullanımı bize zarar getirebilir##
#diyelim ki kullanıcı bize print("Meerhaba dünya") yanıtını verdi
#eval bu veriyi işler ve böyle bir çıktı verir
#merhaba python
#None

#şimdide programımıza open("deneme.txt","w") yazalım
#bu veriyle bilgisayarda deneme.txt adlı bir dosya oluşturduk
#bu yüzdenden program bizim kontrolümüzden çıktı

#normalde biz hesap makinesi programı yazmıştık fakat
#eval() fonskiyonu nedeniyle kullanıcıyal rastgla python komutlarını
#çalıştırma imkanı verdik
#bu yüzdende kötü niyetli kişi zarar verebilir mesala:
#__import__("os").sytstem("dir")

#bu komut sayesinde bulunudğumuz dizinin altındaki tüm dosyaları listeleyebildik

#bu komutlar her zaman masum olmayabilir
#bazı komutlar yüzünden sabt diskimin silinebilir
#yani eval() kullanıcıda tüm imkanı sağlamış oluyor buda tehlikeli bir adım olur

#bu fonksiyonu kullanamk ne kazandırır ne kaybettirir?:

#eval() fonkiyonun kontrol mekanizması olmadığından
#her türlü kodu işler bu yüzden de bizim için tehlike saçar
#fakat kontrol mekanizması kurarak sadece belli işlerde yapmasını sağlayabiliriz

#------------------------------------------

### exec() ####

#exec() eval fonksiyonuna çok benzerdir
#bu fonksiyon sayesinde karakter dizileri içindeki çok kapsamlı 
#python kodlarını işletebiliriz

#örneğin eval() fonskiyonu bir karakter dizisi içindeki değişken
#tanımlama işlemini yerine getiremez. örnek:
#eval("a=45")

exec("a = 45")

print(a)#45

#eval() ve exec() kullanıcıdan alınan verilerle doğrudan işlem
#yapmak gereken durumlarda işimize yarar
#örneğin bir hesap makinesi yapmak için eval() fonskiyonundan yararlanırız

#aynı şekilde python proglama dilini öğreneten bir program için
#exec() kulanabiliriz:

d1 = """
Python'da ekrana çıktı verebilmek için print() adlı
bir fonskiyonundan yararlanıyoruz. bu fonskiyonu şöyle
kullanabilirsiniz:
>>> print("Merhaba Dünya")

şimdi de aynı kodu siz yazın
>>> """
girdi = input(d1)
exec(girdi)
d2 ="""
Gördüğünüz gibi print() fonskiyonu, kendisine parametre
olarak verilen değerleri ekrana basıyor.

böylece ilk dersimizi tamamlamış olduk. şimdi bir sonraki
dersimize geçebilirsiniz."""
print(d2)
#sonuç:
"""
Python'da ekrana çıktı verebilmek için print() adlı
bir fonskiyonundan yararlanıyoruz. bu fonskiyonu şöyle
kullanabilirsiniz:
>>> print("Merhaba Dünya")

şimdi de aynı kodu siz yazın
>>> print("Merhaba Dünya")
Merhaba Dünya

Gördüğünüz gibi print() fonskiyonu, kendisine parametre
olarak verilen değerleri ekrana basıyor.

böylece ilk dersimizi tamamlamış olduk. şimdi bir sonraki
dersimize geçebilirsiniz.
"""
#eval ve exec fonksiyonları ne kadarda kullanışlı gözükselerde
#yanlış kullanımında felakate yol açarlar

#-------------------------------------------------

#### format() Metodu #####

#karakter dizisi biçimlendirme işlemleri için format() methodu kullanırız

#kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazınız: ")
#adresin bulunamadığı konusunda kullanıcıyı bilgilendirelim
print("Hata! Google Chrome {} sitesini bulamadı".format(url))
#Hata! Google Chrome kask.com sitesini bulamadı

#diğer örnekler

print("{} ve {} iyi bir ikilidir.".format("Python","Django"))
#Python ve Django iyi bir ikilidir.
print("{} {}'yi çok seviyor!".format("Ali","Ayşe"))
#Ali Ayşe'yi çok seviyor
print("{} {} yaşında bir {}dur".format("Ahmet","18","futbolcu"))
#ahmet 18 yaşında bir futbolcudur

#bu kodları şu şekilde de yazdırabiliriz
metin = "{} ve {} iyi bir ikilidir"
print(metin.format("Python","Django"))

metin = "{} {}'yi seviyor!"
print(metin.format("Ali","Ayşe"))
#Ali Ayşe'yi seviyor
metin = "{} {} yaşında bir {}dur"
print(metin.format("Ahmet","28","futbolcu"))
#Ahmet 28 yaşında bir futbolcudur

#kullanıcıdan alınan değerlerle dilekçe yazmamız lazım
#dilekçe taslağı:
"""
tarih:

T.C.
... ÜNİVERSİTESİ
... Fakültesi Dekanlığına


Fakülteniz ..........Bölümü ......... numaralı öğrencisiyim. Ekte sunduğum
belgede belirtilen mazeretim gereğince ....... Eğitim-Öğretim Yılı  .........
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

    İmza

Ad-Soyadı       :
T.C. Kimlik No. :
Adres           :
Tel.            :
Ekler           :
"""

dilekce = """ 
tarih: {}


T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına


Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı  {}.
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

        İmza

Ad              : {}
Soyad           : {}
T.C. Kimlik No. : {}
Adres           : {}
Tel.            : {}
Ekler           : {}
"""

tarih          = input("tarih: ")
universite     = input("Üniversite Adı: ")
fakulte        = input("Fakulte Adı: ")
bolum          = input("Bölüm Adı: ")
ogrenciNo      = input("Öğrenci No: ")
ogretimYili    = input("Öğretim yılı: ")
yariyil        = input("Yarıyıl: ")
ad             = input("Öğrencinin adı: ")
soyad          = input("Öğrencinin soyadı: ")
tcKimlikNo     = input("TC Kimlik No: ")
adres          = input("Adres: ")
tel            = input("Telefon No: ")
ekler          = input("EKler: ")

print(dilekce.format(tarih,universite,fakulte,bolum,
ogrenciNo,ogretimYili,yariyil,ad,soyad,tcKimlikNo,
adres,tel,ekler))

"""
T.C.
istanbul üniversitesi ÜNİVERSİTESİ
kimya mühendisliği Fakültesi Dekanlığına


Fakülteniz kimya hocalığı Bölümü 278 numaralı öğrencisiyim. Ekte sunduğum belgede        
belirtilen mazeretim gereğince 2020 Eğitim-Öğretim Yılı  2021.
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

        İmza

Ad              : murat
Soyad           : can
T.C. Kimlik No. : 8792739373638
Adres           : istanbul üniversite karşısı bina
Tel.            : 38393302
Ekler           : kudnaurpakcnuıssad
"""

#metine kullanıcıdan alınacak bilgilerin olduğu yerlere birer {} koyduk
#bu eksiklikleri tamamlayacak veriyi input la kullanıcıdan aldık
#sonra metnin tam halini print fonksiyonuyla yazdırdık

#karakter dizisinin içinde kaç tane {} varsa
#format() metodunun parantezleri içinde o sayıda değer olması gerekir


