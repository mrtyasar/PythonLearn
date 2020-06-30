#Koşul Deyimleri
#------------------------
###### if ###########
#------------------------

#işleç anlamları
# > büyüktür
# < küçüktür
# >= büyük eşittir
# <= küçük eşittir
# == eşittir
# != eşit değildir

# = atama, == eşittir işareti

a = 26
#a değerin içine 26 yı atadık
print(a == 26)#True
#a nın içinde 26 olduğundan 26 ya eşittir bu yüzden True cevabını aldık

n = 200
if n > 10:
    print("Sayı 10'dan büyüktür!")
#sayı 10 dan büyüktür
#n adlı değişkenin içine 200 değeri attık
# if dedik yani eğer dedik n, 10dan büyükse
# sayı 10dan büyüktür ifadesini yazdır dedik

#kullanıcıdan veri alarak yapalım:

sayi = int(input("Herhangi bir sayı giriniz: "))
if sayi > 10:
    print("Girdiğiniz sayı 10'dan büyüktür")
if sayi < 10:
    print("Girdiğiniz sayı 10'dan küçüktür")
if sayi == 10:
    print("Girdiğiniz sayı 10'dur")


#örnek

print("""
Dünyanın en gelişmiş e posta hizmetine
hoşgeldiniz. Yalnız hizmetimizden yararlanmak
için önce sisteme giriş yapmalısınız.""")

parola = input("Parola: ")
if parola == "12345678":
    print("Sisteme Hoşgeldiniz")
if parola != "12345678":
    print("Ne yazık ki yanlış parola girdiniz!")    

#kullanıcıdan parola aldık
#parola dedik 12345678 ise sisteme hoşgeldin de dedik
#eğer 12345678 değilse ise hata mesajı göster dedik

#-------------------------------------
###### elif #######
#-------------------------------------

#elif if gibi koşul deyimidir
#if koşulu gerçekleştirmediyse o zaman bu koşulu gerçekleştir demektir

age = int(input("Yaşınız: "))

if age == 18:
    print("18 iyidir!")
elif age < 0:
    print("Yok canım daha neler") 
elif age < 18:
    print("Genç bir kardeşimsin")
elif age > 18:
    print("eh, artık yaş yavaş yavaş kemale eriyor!")

#bu kodu şu şekilde de yazabilirdik

ageOne = int(input("Yaşınızı giriniz: "))

if ageOne == 18:
    print("18 iyidir")
if ageOne < 0:
    print("Yok canım, daha neler!...")
if ageOne < 18:
    print("Genç br kardeşimizsin")
if ageOne > 18:
    print("eh, artık yaş yavaş yavaş kemale eriyor")

#sürekli if kullanımı veya else kullanımın farkı:
#if bütün olası sonuçları gösterir
#else ise doğru olan sonucu gösterir
#mesala yaşımız her iki kodda da -1 diyelim
#else'nin olduğu kodda çıktı:
#Yok canım daha neler

#if in olduğu kodda çıktı:
#Yok canım, daha neler!...
#Genç br kardeşimizsin

#çünkü else sırasıyla gider
#if gerçekleştirmediyse elif komutu harekete geçer
#buda değilse diğer elif
#buda değilse diğer elif
#ve elif komutu doğru cevabı bulduğunda ise durur ve sonucu gösterir

#if de ise tek tek inceleyip hepsini işleme alıyor bu yüzden
#bazen 2 3 tane doğru cevabı gösterebiliyor


#------------------------------------
###### else ########
#------------------------------------

#else yukarıdaki koşulların hiçbiri gerçekleşmezse çalışır
#yani iki tane koşul koyduk fakat 2 koşulda yoksa else çalışmaya başlar

#örnek

soru = input("Bir meyve adı söyleyin bana: ")

if soru == "elma":
    print("evet,elma bir meyvedir..")
elif soru == "karpuz":
    print("evet,karpuz bir meyvedir...")
elif soru == "armut":
    print("evet,armut bir meyvedir...")
else:
    print(soru,"gerçekten bir meyve midir?")
    #araba gerçekten bir meyve midir

#input fonksiyonu sayesinde kullanıcıdan veri aldık vu veriyide soru değişkeninde
#depoladık
#eğer dedik elmaysa şunu yap
#değilse şunu yazdır
#değilse şunu yazıdr
#değilse şunu yazdır
#yok hiç biride değilse eğer(else) o zaman şunu yazdır dedik

#eğer else bloğunu kullanacaksak ondan önce gelen durumların ilkini zorunlu olarak if ile
#sonrakilerini ise elif ile bağlayın
#yoksa karmaşık cevaplar alırsınız buda istemediğimiz sonuçlar doğurabilir
#örnek:
"""
if koşul1:
    sonuç1
elif kosul2:
    sonuc2
elif kosul3:
    sonuc3
else:
    sonuc4
"""
#eğer else blogundan önce tek bir koşul bloğu yer alacaksa
# bunu ilk başta if ile bağlanmalı:
"""
if kosul1:
    sonuc1
else:
    sonuc2
"""

#örnek

boy = int(input("boyunuz kaç cm?"))

if boy < 170:
    print("boyunuz kısa")
elif boy < 180:
    print("boyunuz normal")
else:
    print("boyunuz uzun")#200 dedik boyunuz uzun cevabı aldık

# if dedik eğer kullanıcın verdiği boy oranı 170 den kısaysa şunu yazıdr dedik
# eğer olmadıysa else dedik boy 180 den küçükse şunu yazdır dedik
# verilen koşullardan hiçbiri gerçekleşmediyse else dedik şunu yazdır dedik

#---------------------------------------
############# Örnek Uygulama ###########
#---------------------------------------

#kullanıcıdan kullanıcı adı ve şifre alacağız
#aldığımız şifre ise 40 karakteri geçmemelidir

kullaniciAdi = input("Kullanıcı adınızı giriniz: ")
parolaName = input("Şifrenizi giriniz lütfen")
toplamUzunluk = len(kullaniciAdi)+len(parolaName)

mesaj = "Kullanıcı adı ve parolanız toplam {} karakterden oluşuyor!"
print(mesaj.format(toplamUzunluk))
if toplamUzunluk < 40:
    print("Sisteme Hoşgeldiniz:")
else:
    print("Kullanıcı adınız ile parolanız ",
    "toplam uzunlığu 40 karakteri geçmemlidir")


