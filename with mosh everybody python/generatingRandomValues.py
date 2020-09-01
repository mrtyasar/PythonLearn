# Pythonda yerleşik olarak bulunan ve her türlü ihtiyacığımızı giderebilen modüller vardır
# bu modüllerin hepsine bakmak için google a şu şekilde aratabiliriz
# python 3 module index
# python un sürümünü belirtin yoksa python 2 modülleri de çıkabilir

# örneğin tarihle ilgili bir işlem yaptığımızda datetime modülünü kullanabiliriz
# veya e maillerle ilgiili bir işlem yaptığımızda email modülünü kullanabiliriz

# peki modülleri nasıl kullanabileceğiz: 

# import yoluyla modülü içeri aktar
import random

# random modülü rastgale değer üretmeyi sağlayan bir modüldür
for i in range(3):
    print(random.random())

# random.random() diyerek random modülün random() özelliğine erişebildik
# random() işlevi ise 0 ile 1 arasında rastgale bir sayı üretir bkz: 0.9811355634797027 

# peki ya 0 1 arası değilde farklı sayılar arasında rastgale sayı nasıl üretebileceğiz
# randint() işlevi ile

for i in range(3):
    print(random.randint(20,40))

# 20 ile 40 arasında rastgale sayı ürettik

# choice() işlevi karakter dizilerinde, tuple veya liste vb. gibi yerlerde
# rastgele olarak bir öge döndürür

members = ['John','Mary','Bob','Mosh']
leader = random.choice(members)
print(leader)


# EGZERSİZ

# zar oyununu yap

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
print(dice.roll())