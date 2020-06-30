#----------------------------------------------#
# Karakter Dizilerinin İçeriğini Karşılaştırma
#----------------------------------------------#

#elimizde iki farklı metin var
ilkMetin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinciMetin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

#programımızda ilkMetin de olup ikinciMetin de yer almayan öğeleri ayırmak istiyoruz
for s in ilkMetin:#ilkMetin'deki s adını verdiğimiz her bir öğe için
    if not s in ikinciMetin: #eğer s adlı bir öğe ikinciMetin de yoksa
        print(s)#s adlı öğeyi ekrana yazdır
        #a
#a
#ş
#ş
#a

#ikinciMetin de olan fakat ilkMetin de olmayan öğeleri bulalım
for m in ikinciMetin:
    if not m in ilkMetin:
        print(m)

#u ı o r y e u ı r u e e e u

#birden fazla aynı öğenin yazılmasını istemiyorsak
fark = ""
for p in ikinciMetin: #ikinciMetin de p dediğim bütün öğeler için
    if not p in ilkMetin: # eğer p ilkMetin in içide yoksa
        if not p in fark: # eğer p öğesi fark yoksa
            fark += p#bu öğeyi fark değişkenine ekle
print(fark)#u ı o r y e


#eğer karakter dizi ile birleşirme gerçekleştiriyorsak bu işlem değişkenin önceki değerini değiştirmez
a = "istihza"
print(a + ".com")#istihza.com
print(a)#istihza

#bu işlemin kalıcı hale getirmek için ise yeni işlemi yeni bir değişkene atayarak yaparız
a = a +".com" # a += ".com" olarakda yazabilirdik
print(a)#istihza.com

#yukarıdaki işlemi şöyle kolayca da yazabilirdik:
firstString = "asadlaskdnlnceıfeşsdje9"
twoString = "asşdlmasejmşşvawldad"
cikarma = ""
for e in firstString:
    if not e in twoString and not e in cikarma:
        cikarma  += e
print(cikarma)#k n c ı f 9

"""
#--------------------------------------#
# DOSYALARIN İÇERİĞİNİ KARŞILAŞTIRMA
#--------------------------------------#

#değişkenlerimizi karşılaştırmıştık
#şimdi ise dosyaları karşılaştıralım
#elimizde isimler1.txt ve isimler2.txt adlı iki dosya var

d1 = open("isimler1.txt")#dosyayı açıyoruz
d1Satirlar = d1.readlines() #satırları okuyoruz

d2 = open("isimler2.txt")#dosyayı açıyoruz
d2Satirlar = d2.readlines()#satırları okuyoruz

for i in d2Satirlar:
    if not i in d1Satirlar:
        print(i)

d1.close()
d2.close()
"""
#-----------------------------------------#
# KARAKTER DİZİSİNDEKİ KARAKTERLERİ SAYMA
#-----------------------------------------#

#metin de her harfin kaç kere geçtiğini gösteren program:
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("Sorgulamak istediğiniz harf: ")

number = ""

for l in metin: #metin in içinde s adını verdiğimiz her bi öğe için:
    if harf == l: #eğer kullancıdan gelen harf l ile aynıysa
        number += harf #kullanıcıdan gelen bu harfi sayı değişkenine ata
print(len(number))   

#eğer 5 tane a varsa number değişkenine aaaaa yazar
#print fonksiyonu sayesinde number ın eleman sayısını öğreniriz

#bunun yerine şöyle de yazabiliriz

metinOne =""" Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır."""

harfOne = input("Sorgulamak istediğin harf:")
sayi = 0
for i in metinOne:
    if harfOne == i:
        sayi += 1
print(sayi)        

#eğer kullanıcıdan gelen harf kullanıldıysa ona bir ekle diyoru 
#böylelikle o harf kaç kere kullanıldıysa sayinin değeri 1 artacak


#-----------------------------------------------#
# DOSYA İÇİNDEKİ KARAKTERLERİ SAYMA
#-----------------------------------------------#

#bir önceki metnin değişken olarka değilde dosya içinde okunan bir metin farzedelim

hakkinda = open("hakkında.txt",encoding="utf-8")#dosyamızı açıyoruz
#harfTwo = input("Sorgulamak istenilen harf") #kullanıcıdan harf istiyoruz
sayiOne = 0 #değerini sıfır yapıyoruz
for karakterDizisi in hakkinda: #dosyanın içindeki karakterDizi adlı her bir öğe için
    for karakter in karakterDizisi: #karakterDizisinin karakter adlı her bir öğe için
        if harfTwo == karakter: #eğer kullanıcın verdiği harf karaktere eşitse
            sayiOne += 1 # sayiOne değerine 1 ekle
#print(sayiOne) #ekrana sayiOne yazdır
hakkinda.close() #bütün işlemleri kaydetmek için dosyayı kapatıyoruz
#eğer bir satırın ayrı bir karakter dizisi olduğunu görmek için repr() yararlanırız
"""
for karakterDizisi in hakkina:
    print(repr(karakterDizisi))

Çıktı:
'Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı\n'
'tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,\n'
"""
"""
Bu çıktıya çok dikkatlice bakın. repr() fonksiyonu sayesinde Python’ın alttan alta neler çevirdiğini bariz bir biçimde görüyoruz. Karakter dizisinin başlangıç ve bitişini gösteren tırnak işaretleri ve \n kaçış dizilerinin görünür vaziyette olması sayesinde her bir satırın ayrı bir karakter dizisi olduğunu daha net bir şekilde görebiliyoruz.

Biz yazdığımız kodlarda, kullanıcıdan bir harf girmesini istiyoruz. Kullandığımız algoritma gereğince bu harfi metindeki karakter dizileri içinde geçen her bir karakterle tek tek karşılaştırmamız gerekiyor. input() metodu aracılığıyla kullanıcıdan tek bir karakter alıyoruz. Kullandığımız for döngüsü ise bize bir karakter yerine her satırda bir karakter dizisi veriyor. Dolayısıyla mesela kullanıcı ‘a’ harfini sorgulamışsa, ilk for döngüsü bu harfin karşısına ‘Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcın’ adlı karakter dizisini çıkaracaktır. Dolayısıyla bizim bir seviye daha alta inerek, ilk for döngüsünden elde edilen değişken üzerinde başka bir for döngüsü daha kurmamız gerekiyor. Bu yüzden şöyle bir kod yazıyoruz:
"""
"""
for karakter_dizisi in hakkında:
    for karakter in karakter_dizisi:
        """



                                            




























