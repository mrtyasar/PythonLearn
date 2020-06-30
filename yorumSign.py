#yazdığımız kodlar okunaklı olmalı ve karmaşık olmamalıdır

isim = "Murat"
soyisim = "Can"
isletim = "Windows 10"
sehir = "İstanbul"

print("isim:  ",isim,"\n","Soyisim:  ",soyisim,"\n",
"İşletim Sistemi:  ",isletim,"\n","Şehir:  ",sehir,"\n",sep="")
"""
isim:  Murat
Soyisim:  Can
İşletim Sistemi:  Windows 10
Şehir:  İstanbul
"""
#bu şekilde yazmak bir hataya neden olmaz fakat daha sonra kodlarımıza bakınca
#bize karmaşık gelebilir bu yüzden okunaklı bir biçimde yazabiliriz:

print("İsim            : ",isim,    "\n",
      "Soyİsim         : ",soyisim, "\n",
      "İşletim sistemi : ",isletim, "\n",
      "Şehir           : ",sehir,   "\n",sep="")

          
"""
 İsim            :  Murat
 Soyİsim         :  Can
 İşletim sistemi :  Windows 10
 Şehir           :  İstanbul
"""

#yorum satırları

#yorum satırları tek satır için # birden fazla satır için """ """ kullanılır
#yorum eklemek kodun okunurluğunu arttırır
#hem uzun zaman sonra tekrar bakacağımız kodları anlamak 
#hemde farklı kişilerin bizim kodları anlamamız için yorum satırı eklememiz lazım
#yorum satırı eklediğimizde dikkat etmemiz gerekenler:
#kodu tanımlayan kısa bir cümle yeterlidir
#uzun uzun bütün bir kodun her tarafına yorum satırı eklemek işi zorlaştırabilir

#örneğin bir değişken tanımladık ama bizim için yakın başkası için uzak bir kelime kullandık
#bu değişken adının neyi temsil ettiğini belirtebiliriz
#diyelim ki:
# sep="" yazdık bunu şöyle açıklayabiliriz 
# #parametreler arasında boşluk bırakmıyoruz

"""
Yorum İşaretinin Farklı Kullanımları
"""
#yorum işaretini çoğunlukla kodu açıklamak için kullandık
#fakat başka amaçlar için de kullanabiliriz

#ETKİSİZLEŞTİRME AMAÇLI

name = "Murat"
surName = "Can"
#city = "İstanbul"

print("İsim : ",name,"\n",
      "Soyisim: ",surName,"\n",
      #"city:",city,sep="" 
    sep="")
"""
İsim : Murat
Soyisim: Can
"""

#burada programa henüz eklemeyeceğimiz bir değer girdik
#şimdilik kullanmayacağımız için yorum satırı yaptık
#bu sayede biz görsekte python bu kodu görmeyecek
#ekleme zamanı geldiğinde yorum satırını kaldırmak yeterlidir


#SÜSLEME AMAÇLI

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                    FALANCA v.1                      #
#                Yazan: Keramet Su                    #
#                  Lisans: GPL v2                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

print("Bölüm sonu")

#kodumuzu süslemek amaçlı kullanabiliriz
#fakat unutmamak gerek yorum işaretlerini yerinde ve makul sayıda kullanamk en iyisidir
