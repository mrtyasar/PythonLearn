#else deyimi döngülerle beraber kullanınca break deyiminin işini yapar

for i in range(5):
    print(i)
else:
    print("Else çalıştı")#01234Else çalıştı

#burada döngüyü kırıp programı kapattı

#eğer döngünün içinde break varsa break önceliğe sahiptir ve else çalışmaz

a = 0
while True:
    a += 1
    print(a)
    if a == 3:
        break
else:
    print("Else çalıştı")#123

karakterDizisi = "Merhaba Dünya!"
for harf in karakterDizisi:
    if harf == "a":
        print("a harfi bulundu.")
#a harfi bulundu
#a harfi bulundu
#a harfi bulundu

#eğer ilk a harfine rastlandığında durmasını istiyorsak break i kullanabiliriz

#a harfi bulunmadı yazdıralım

strgingOr = "Bu yAzıdA küçük A yoktur"
for u in strgingOr:
    if u == "a":
        print("a harfi bulundu.")
        break
else:
    print("a harfi bulunmadı.")   # a harfi bulunmadı






















