while True:
    s = input("Bir sayı giriniz: ")
    if s == "iptal":
        break
    if len(s) <= 3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz.")

#eğer kullanıcı iptal yazarsa programdan çıkacaktır
#eğer kullanıcı 3 basamaklı veya daha az haneli bir sayı girerse
#tekrar programın başına dönecek ta ki kullanıcı iptal yazana kadar
#oldu ki 3 ten daha büyük basamaklı sayı yazarsa print fonskiyonu çalışacak

#yani continue koşulu true olduğu zaman kendisinden sonra gelen kodları etkisiz hale getirir
#programa döner durur




























