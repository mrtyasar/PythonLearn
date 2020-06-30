#break deyimini çoğunlukla döngülerde kullanırız
#break kelime anlamı gibi bir akışı bozmak kırmak işlemini yapar
#yani bir döngünün sonsuz döngüye uğramaması için break deyimini kullanırız 
#ki döngüyü kırsın ve program kapansın

while True:
    parola = input("Parolanızı belirleniniz: ")
    if len(parola) < 5:
        print("Parolanız 5 karakterden az olamaz")
    else:
        print("Parolanız belirlenmiştir: ",parola)
        break
           

#eğer kullanıcının belirlediği parolanın eleman sayısı 5 ten küçükse şunu yap dedik
#onun haricinde parolayı göster dedik ve break ile döngüden çıkıp programı kapattık

#ayrıca break deyimi her zaman döngünün içinde yer alması gerekiyor
#aksi takdirde hata alırız


































