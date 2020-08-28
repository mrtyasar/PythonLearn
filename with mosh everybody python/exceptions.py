# bu derste pythonun bize gösterdiği hataları nasıl çözeriz onu göreceğiz

age = int(input('Age: ')) # kullanıcıdan veri al bu veriyi int değerine çevir ve age değişkenine at
print(age) # 20 # age değişkenini ekrana yazdır

# sayısal değerler girince herhangi bir sorun elde etmiyoruz
# fakat sayısal değil karakter dizisi girersek ne olur?

# ValueError hatası alırız
# bunun nedeni inputtan gelecek veriyi int() tipine çevirmemiz
# ve girdiğimiz karakter dizisi sayısal bir değere dönüştürelemeyeceği için
# bilgisayarın kafası karışıyor ve ValueError hatası alıyoruz

# hatalar programamızın çökmesine sebebiyet verir
# bu durumu engellemek için try.. except.. den yararlanabailiriz

try:
    age1 = int(input('Yaşınız kaçtır? '))
    print(age1)
except ValueError:
    print('Lütfen sadece sayısal değer giriniz!') 

# hata üreteceğini düşündüğümüz kodları try bloğunda yazarız
# eğer bir hata oluşursa except hataİsmi yazarak kod bloğuna hata çıktısını yazdırabiliriz

# bu sayede kodumuz hata üretip programımız çökeceğine
# işimizi sağlama alıp hatayı sadece except ile bertaraf edebiliriz

# eğer except de hata ismini belirtmezsek tüm hatalara aynı hata mesajı yazdırırız

"""
Formül:

try:
    hata üreteceğini düşündüğümüz
    kodlar
except hataİsmi:
    hata üretildiğinde hatanın yerine geçecek hata mesajı
"""

try:
    name = float(input('Lütfen adınızı giriniz: '))
    print(name)
except:
    print('Hata yaptınız! tekrar kontrol ediniz...')

# sadece except yazdırarak tüm hatalara tek bir cevap verebildik
# bunun bir avantajı birde dezavantajı vardır
# avantajı tek tek hata isimlerini yazmadan tüm hataları yok edebiliriz
# dezavantajı tüm hataları tek bir mesajla temsil ettiğimiz için
# kullanıcaya hata hakkında bir bilgi vermiyoruz

try:
    print('20 sayısını bölünüz... ')
    sayi = int(input('bölecek sayı: '))
    bolunecek = 20
    print(bolunecek / sayi)
except ZeroDivisionError:
    print('Bir sayıyı 0 ile bölemezsiniz!')