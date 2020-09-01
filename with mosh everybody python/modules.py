# converters.py isimli yeni bir dosya oluşturduk

# modüller içinde belli özellikleri taşıyan kodları kolayca içeri aktararak
# kullanabilmemizi sağlar

# bu derste ise yeni bir modül yaratarak onu içeri aktarmayı öğreneceğiz
# sadece dosyanın adını yazmamız yeterlidir py eklememize gerek yoktur

import converters

print(converters.kgToLbs(70))

# modülleri aktarırken sadece tüm modülü değil modülün içindeki herhangi bir özelliğini
# aktarabiliriz

from converters import kgToLbs

print(kgToLbs(70))

 # import converters

# veya direk özelliği ekleyebiliriz

from converters import find_max
numbers = [20,35,4,100]
print(find_max(numbers))