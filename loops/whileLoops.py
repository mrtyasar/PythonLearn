#while ile olduğu sürece bunu yap diyebiliyoruz
#örneğin
a = 1
"""
while a == 1:
    print("Bilgisayarım Çok Güzel!")
"""
#makineye a değişkenin değeri 1 olduğu sürece Bilgisayarım çok güzel
#yazsını yazdır diyoruz

#fakat bir sıkıntı varki makine bu komutun sonunu algılayamadığı için sürekli bunu yazdıracak
#yani sonsuz döngüye girmiş olacak
#bunu engellemek için ise: 

while a < 10:
    a += 1
    print("Bilgisayarım Çok güzel")

"""
makineye a değeri 10'dan küçük olduğu müddetçe bunu yazdır dedik
fakat bundan önce ise a += 1 dedik yani a nın değerini her aşama 1 yükseltiyoruz
ki makine 10 a gelince durdun
makine her işlemde a nın değerini bir yükseltecek print fonskiyonunu çalıştıracak
sonra bir daha yükseltecek yine printi çalıştırcak
ta ki değer 10'dan küçük olduğu sürece
"""

a = 1
while a < 10:
    a += 1
    print(a) # 2 3 4 5 6 7 8 9 10


#while ile toplama ve çıkarma işlemi yapan bir hesap makinesi yapalım

giris = """
(1) topla
(2) çıkar
"""
print(giris)

theEnd = 1
while theEnd == 1:
    soru = input("Yapmak istediğiniz işlemin numarasını giriniz(Çıkmak için q): ")
    if soru == "q":
        print("Çıkılıyor....")
        theEnd = 0
    elif soru == "1":
        sayi1 = int(input("Toplama işlemi için ilk sayıyı giriniz: "))
        sayi2 = int(input("Toplama işlemi için ikinci sayıyı giriniz: "))
        print(sayi1,"+",sayi2,"=",sayi1+sayi2)
    elif soru == "2":
        sayi3 = int(input("Çıkarma işlemi için ilk sayıyı giriniz: "))
        sayi4 = int(input("Çıkarma işlemi için ikinci sayıyı giriniz: "))
        print(sayi3,"-",sayi4,"=",sayi3-sayi4)
    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:",giris)

#burada theEnd 1 olduğu sürece bu işlemi yap dedik
#sonsuz döngüye girmesin diye ise eğer soru eşitse "q" değerine
#şunu yazdır dedik ve programın durması için ise theEnd in değerini 0 yaptık
#burada q demediğimiz sürece program çalışmaya devam edecektir

#theEnd in değerini istediğimiz değer koyabiliriz zorunlu olarak 0 veya 1 yoktur

anahtar = "Hoyda bre!"
#anahtarın değeri "Hoyda bre!" olduğu müddetçe aşağıdaki blogu
#çalıştırmaya devam et
while anahtar == "Hoyda bre!":
    soruOne = input("yapmak istediğiniz işlemin numarasını giriniz(çıkmak için q):")
    if soruOne == "q":
        print("Çıkıyorsunuz şimdi...")
        anahtar = "Dur yolcu!"
        #anahtarın değeri artık hayde bre değil dur yolcu oldu

#bu işlemi şöyle daha basit bir şekilde yazabilirdik:


while True:
    name = input("Adınızı giriniz lütfen(Çıkmak için q): ")
    if name == "q":
        print("Çıkıyorsunuz.....")
        break

#bu işlem sayesinde değişken atama işleminden kurtuluyoruz
#while true olduğu sürece çalıştır diyoruz
#buradaki True nun anlamı aslında aksi belirtilmediği sürece çalışmaya devam et
#demektir
#yani bir break işlemi yapmasaydık sürekli o input fonksiyonu çalışacaktı

#buradaki break in görevi ise döngüyü kapatmak kırmak veya sonlandırmaktır
#bir örnek daha:

#aksi belirtilmediği sürecek kullanıcıya
#aşağıdaki soruyu sormaya devam et
while True:
    soruOr = input("Nasılsınız, iyi misiniz?")
    #eğer kullanıcı "q tuşuna basarsa..
    if soruOr == "q":
        break #döngüyü kır ve programdan çık

"""mantık kısaca:
   Bir döngü oluştur ve bu döngüden çıkmak istediğinde, 
   programın bir yerinde bu döngüyü sona erdirecek bir 
   koşul meydan getir. 
"""
#yani
"""
while True: ifadesi yardımıyla bir döngü oluştur ve kullanıcı 
bu döngüden çıkmak istediğinde (yani q tuşuna bastığında), 
döngüyü kır ve programı sona erdir.
"""
#deneme:

tekrar = 1
while tekrar < 3:
    print("Tekrar",tekrar)
    tekrar += 1
    input("Nasılsınız iyi misiniz")
    print("bool değeri:", bool(tekrar <= 3))
"""
Nasılsınız, iyi misiniz?q
Tekrar 1
Nasılsınız iyi misinizq
bool değeri: True
Tekrar 2
Nasılsınız iyi misinizq
bool değeri: True
"""
#print fonksiyonu sayesinde arkada neler döndüğünü öğrendik
#bu taktiği çoğu kez işlerin nasıl ilerlediğini anlamamıza sağlar
#buradaki bool ise true mu false mi çevirdiğini gösteriyor
#yani burada makine 3 ü görünce false verdiğini görüyoruz

#while döngüsünü kullanarak 1'den 100 e kadar olan aralıktaki çift sayıları bulalım

b = 0

while b < 100:
    b += 1
    if b % 2 == 0:
        print(b)

#burada b değeri 100 den küçük olduğu sürece 1 arttır
#bunun sebebi b nin değeri 100 e ulaşsın ve sonsuz döngüye girmeşsin
# eğer dedik b değerinin 2 ye bölünüp kalanı 0'a eşit ise b yi yazdır
#böylece makine sadece çift sayıları yazdırmış olacak















