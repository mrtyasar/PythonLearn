# Paketler çok fazla modulü bir arada toplayarak dağınık olmamızı
# engelleyen bir yapıdır

# mesala ecommerce adlı bir packages oluşturduğumuzda e ticaret ile ilgili
# işlevleri, modüllerileri, kodları burada toplayabiliriz

# ecommerce adlı bir paket oluşturduk
# pythonda kuraldık paketlerde __init__.py adlı bir dosya olur
# çoğu ide bunu otomatik olarak ekler ama yoksa elle de eklenebilir

# shipping.py adlı bir file oluşturduk içine bunları yazdık

"""
def calc_shipping():
    print('calc_shipping')
"""

# paketin içindeki modülleri veya modüllerin içindeki özellikleri nasıl çağırabiliriz?:

# modülleri şu şekilde çağırabiliriz:

"""
import ecommerce.shipping

ecommerce.shipping.calc_shipping()

output:
calc_shipping
"""

# bir diğer yöntem ise from kullanarak çağırabiliriz

"""
from ecommerce.shipping import calc_shipping, calc_text

calc_shipping()
"""
# bu sayede daha kısa bir şekilde kodumuzu kullanabiliriz
# eğer birden fazla özelliği eklemek istiyorsak virgülleri kullanarak ekleyebiliriz ^ 

# veya modülün içindeki tüm özellikleri çağırabiliriz

"""
from ecommerce import shipping

shipping.calc_shipping()
"""


