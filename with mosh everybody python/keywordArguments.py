def username(firstName,lastName):
    print('Hello!')
    print(f'Hello {firstName} {lastName}')

# keyword Arguments kodda parametrelerin sıralarınışını belirleyebiliriz
username(lastName='can',firstName='murat')

# Anahtar kelimeleri çoğunlukla kodların okunaklığı için kullanırız
# örneğin fazlasıyla sayısal değerler kullanıyorsak bu değerleri anlatmamız
# daha sonra baktığımızda neyi temsil ettiklerini anlamamız için kullanabiliriz

fiyatListesi(kalemler=50,defterler=100,silgiler=25)
# anahtar kelimeleri kullanarak değerlerin neyi temsil ettiklerini açıkca gösterebildik

