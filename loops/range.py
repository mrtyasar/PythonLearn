#range fonksiyonu bir sayı ile başka bir sayının arasındaki sayıları yazdırır
#formül
# range(ilk sayı, son sayı)

for i in range(0,10):
    print(i)# 0123456789

#range fonskiyonun ilk paramateresi 0 olacaksa belirtmemize gerek yoktur
for m in range(13):
    print(m)#0123456789101112

for n in range(3,11):
    print(n)#345678910

#3 karakter kısa 8 karakterden uzun parola berillenmesini engelleyen program:
while True:
    parola = input("Parolanızı Belirleyiniz: ")
    if not parola:
        print("Parola bölümü boş geçilemez!")
    elif len(parola) in range(3,8):
        print("Yeni parolanız: ",parola)
        break    
    else:
        print("Parola 8 karakterden uzun 3 karakterden kısa olmamalı.")
#aksi belirtiylmediği sürece bunu yap dedik
#eğer parola boş sa bunu yap dedik
#oda değilde parolanın eleman sayısının 3 ten 8 aralığındaysa
#parolayı yazdır dedik ve döngüye girmemesi için break dedik
#hiçbiri de değilse şunu yap dedik

#range fonksiyonu ile bir döngünün kaç kez çalışacağını belirleyelim

for u in range(3):
    print(u)
    sifre = input("Parola belirleyin: ")
    if not parola:
        print("Parola bölümü boş geçilemez!")
    elif len(sifre) in range(3,8):
        print("Yeni parolanız",sifre)
        break
    elif u == 2:
        print("Parolayı 3 kez yanlış girdiniz.",
        "Lütfen 30 dakika sonra tekrar deneyin!")
    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamamlı.")

#range fonksiyonun 3 parametre alabilir
# range(ilk sayı,sonsayı,atlama sayısı)

for y in range(0,10,2):
    print(y)#02468

#sayıları tersten yazdırmak için
for l in range(10,0,-1):
    print(l)#10987654321

for w in range(10,0,-3):
    print(w)#10741

#range() fonskiyonu yıldızlı parametreyi kullanmak
print(*range(10))# 0 1 2 3 4 5 6 7 8 9

#sep parametresiyle kullanmak
print(*range(10),sep=", ")#0, 1, 2, 3, 4, 5, 6, 7, 8, 9



















