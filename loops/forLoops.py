harfler = "asdfgh"
for harf in harfler:
    print(harf)
"""
a
s
d
f
g
h """
#harfler değişkenin içindeki her bir öğeyi ekrana tek tek yazdırdık

"""
for değişkenAdi in değişken:
    yapilacakİşlem

#burada makineye değişken içindeki her bir öğeyi değişkenAdi içine yazdır
#ve bu öğelerle bir işlem yap dedik
"""
#bu işlemi print fonksiyonuyla da yapabilirdik
print(*harfler,sep="\n") #aynı sonucu aldık

#bu işlemi while de yapabilirdik

a = 0
while a < len(harfler):
    print(harfler[a],sep="\n")
    a += 1 #aynı sonucu aldık

#kısaca for while ile çoğunlukla aynı işlemi yapar
#tek fark while yolu daha çok uzatır ve for daha yeteneklidir

#for döngüsünü kullanarak sadece karakter dizileriyle döngü yapabiliriz
sayilar = 12345678
#for sayi in sayilar:
#    print(sayi)

#File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not iterable
#hata aldık çünkü for döngüsünü sayılarla kullanamayız

sayilar = "12345678"
for sayi in sayilar:
   print(int(sayi)*2,end=" ")#2 4 6 8 10 12 14 16

#sayilar değişkeni içine değer atadık
#daha sonra sayilar içindeki her bir öğeyi sayi içine ata
#matematiksel işlem yapacağımız için int veri tipine çevirip ekrana yazdırdık
#alt alta yazılmasın ve aralarına boşluk kalması için end i boş bir karakter dizi koyduk

#yani for her bir öğenin üzerinde etki etki eder

#for ve in ne demek :
#for "için demektir"
#in ise yeri geldiğinde aitlik işleci olarakta kullanılabilir
#in in o anlamdaki anlamı: bir öğenin bir veri tipinin içinde bulunup bulunmadığını
#kontrol ederdi:
b = "istihza.com"
print("h" in b)#True # b nin içinde "h" var mı?
print("b" in b)#False # b değişkenin içinde "b" var mı?

#yani in ingilizcede içinde anlamına geliyor

for s in "istihza":
    print(s) #alt alta: i s t i h z a

#burada "istihza" karakter dizisini s içinde ata
#ve s değişkenin her bir öğe için: ekrana yazdır diyoruz

numbers = "12345678"
for i in numbers:
    if int(i) > 3:
        print(i) # 4 5 6 7 8

#numbers değişkeni içinde i adını verdiğimiz her bir öğe için
#eğer sayıya dönüşütürülmüş i değeri 3'ten büyükse:
#i öğesini ekrana bastır

trHarfler = "şçöğüİı"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter in trHarfler:
        print("parolada Türkçe karakter kullanılamaz")
    else:
        print("Parolanız sisteme uygundur!")
        break    
#burada trHarfler adlı değişkenin içine "şçöğİı" değerini atıyoruz
#kullanıcıdan parolasını girmesini istiyoruz
#parola değişkenin içinde karakter adını verdiğimiz her bir öğe için
#karakter değişkenin öğeleri trHarfler içinde geçiyorsa
#ekrana şunu yazdır
#eğer hiçbir koşul durum gerçekleşmediyse şunu yazdır dedik
#en sonda döngüye girmesini engellemek için break ile sonlandırdık

#kullanıcının belirlediği parolanın 8 karakterden uzun 3 karakterden kısa
#olmamasını sağlayalım

while True:
    parola = input("Bir parola belirleyiniz: ")
    if not parola:
        print("parola bölümü boş geçilemez")
    elif len(parola) > 8 or len(parola) <3:
        print("parola 8 karakterden uzun, 3 karakterden kısa olmamalı")
    else:
        print("Yeni parolanız: ",parola)
        break        

#aksi belirtilmedikçe programın çalışmasını ve kullanıcıya şunu sormasını istedik
#eğer kullanıcı bir şey girmden entera tıklarsa şunu yazdır dedik
#bu durum gerçekleştirmediyse eleman sayısı 8 den büyük veya 3 ten küçük ise
#şunu yazdır dedik
#hibir durum gerçekleşmemişse parolasını gösterdik
#döngüye girmesini engellemek için break dedik

#eval() ı güvenli şekile kullanmak

izinliKarakterler = "0123456789+-/*= "
print("""
Basit bir hesap makinesi uygulaması.
İşleçler: 
 + Toplama
 - Çıkarma
 * Çarpma
 / Bölme

Yapmak İstediğiniz işlemi yazıp ENTER tuşuna
basınız. (Örneğin 23 veya 46 sayılarını çarpmak için
23 * 46 yazdıktan sonra ENTER tuşuna basınız.)""")

while True:
    veri = input("İşleminiz: ")
    if veri == "q":
        print("Çıkılıyor...")
        break
    for v in veri:
        if v not in izinliKarakterler:
            print("Neyin Peşindesiniz?!")
            quit()
    hesap = eval(veri)
    print(hesap)
# while True yani aski belirtilmediği sürece kullanıcıya şunu sor dedik
#eğer kullanıcı "q" ya basarsa şunu göster ve döngüden çık dedik
# veri değişkenin içindeki v adını verdiğimiz her bir öğe için
# eğer v nin içinde izinliKarakterler değişkenin içinde bulunan öğeler bulunmuyorsa
#şunu göster dedik ve quit() fonskiyonuyla programdan tamamen çık dedik
# eval fonskiyonu sayesinde matematiksel işlemler yapabiliriz
#böylece kullanıcı belirlemediğimiz karakter dışında bir şey yazarsa program çıkış yapacak


























