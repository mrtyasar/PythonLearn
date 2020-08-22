# if elif else gibi koşulları destekleyen mantıksal operatörler vardır
# bunlar and or ve not dır

# and operatörü tüm koşul gerçekleşiyor yani tümü doğru ise kod bloğunu çalıştırır
# içlerinden biri yanlış ise komple yanlış olarak algılanır

hasHighİncome = False
hasGoodCredit = True

if hasHighİncome and hasGoodCredit:
    print('Eligible for loan')


# or operatöründe her iki koşuldan bir tanesinin doğru olması yeterlidir.

if hasHighİncome or hasGoodCredit:
    print('Eligible for loan')

# and : tüm koşullar doğru olmalı
# or : en az bir tane koşul doğru olmalı
# not: değer yanlış ise doğru yapar
# not yok değildir anlamındadır eğer a boş ise not a dediğimizde bunun değeri True olacaktır
# bunun nedeni a boş mudur sorusunu sormamız cevap boş evet o zaman True

goodCredit = True
criminalRecord = False

if goodCredit and not criminalRecord:
    print('Krediyi alabilirsiniz!')

