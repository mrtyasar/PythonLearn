# pass deyimini herhangi bir işlemin gerekmediği yerlerde kullanırız
# pythonda görmezden gel hiçbir şey yapma demektir

while True:
    parola = input("Parolanızı belirleyiniz: ")
    if not parola:
        pass
    elif len(parola) in range(3,8):
        print("Yeni parolanız: ",parola)
        break
    else:
        print("Parola 8 karakterden uzun 3 karakterden kısa olmamalı.")

#burada pass ı kullanırken makineye eğer kullanıcı boş geçerse görmezden gel
#programın çalışmasını sürdür diyoruz

while True:
    sayi = int(input("Bir sayı giriniz: "))
    if sayi == 0:
        break
    elif sayi < 0:
        pass
    else:
        print(sayi)

#eğer kullanıcı 0 girerse break deyimi araya girer ve programı sondlandırır
#eğer kullanıcı 0 dan küçük eksili değer girerse pass deyimi çalışır ve program yinede çalışır

#pass ı deyimini taslaklar içinde kullanabilinir
#yani bir kod yazıyorsun fakat koddan emin değilsin o zaman pass ı kullanarak
#kodun çalışmasına engel olmazsın

"""
if .....:
    böyle yap
elif ....:
    böyle yap    
else:
    pass
"""
#elseye pass dedik çünkü else blogunda ne yapacağımızı karar veremedik





























