# bilgisayarın oluşturduğu gizli numarayı tahmin etme oyunu

import random

due = 1
computerRandom = random.randint(0,10)

while due <= 3:
    kullaniciSecimi = int(input("0'dan 10'a kadar bir tahminde bulununuz: "))
    due += 1
    if kullaniciSecimi == computerRandom:
        print('Doğru tahminde bulundunuz!')
        print(f'Bilgisayarın seçtiği sayı:{computerRandom}\nSizin seçtiğiniz sayı {kullaniciSecimi}')
        quit()
    else:
        print('Yanlış bildiniz. Tekrar deneyiniz!')
        print(f'Bilgisayarın Seçtiği sayı: {computerRandom}')
print('Hakkınız dolmuştur! Oyunu tekrardan başlatınız...')  


# Öğretmenin yaptığı kod:

secretNumber = 9 # Bizim seçtiğimiz rakamdır
guessCount = 0 # döngünün başlayacağı sayı
guessLimit = 3 # döngünün biteceği sayı
while guessCount < guessLimit: # guessCount guessLimit küçük olduğunda bunu yap
    guess = int(input('Guess: ')) # kullanıcıdan veri al
    guessCount += 1 # kullanıcıdan her bilgi aldığından guessCount 1 arttır
    if guess == secretNumber: # eğer kullancının sayısı secretNumber a eşitse
        print('You won!') # You won yazısını ekrana yazdır
        break # koşul gerçekleştiğinde döngüden çık
else: # koşul gerçekleşmediyse eğer While döngünün sonunda bunu yap
    print('Sorry, you failed!') # ekrana sorry you failed yazısını bastır

# else yi if bloğunda yazmadık çünkü her bilinmediği takdirde you failed yazısı gözükecek
# bunun yerine else yi while döngünün bloğuna yazdırdık ki kullanıcı
# 3 hakkını doldurduktan sonra kaybettin yazısı çıksın





