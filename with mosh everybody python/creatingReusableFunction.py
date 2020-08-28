def emojis(message): # emojis adlı fonksiyon oluşturduk message adlı parametre oluşturduk
    words = message.split(' ') # parametre olarak girilen verinin boşluktan bölerek tek tek ayırıyoruz
    emojis = {
        ':)':'😊',
        ':(':'😢'
    } # kullanıcı eğer bu ifadeleri yazarsa bu emojilere denk olduğunu belirtiyoruz
    output = '' # boş karakter dizisini değişkenin içine attık
    for word in words: # her bir ögeyi tek tek işleme almak için for döngüsü kurduk
        output += emojis.get(word,word) + ' ' 
    return output # output değişkenini döndür
message = input('> ') # önce kullanıcıdan veriyi alıyoruz
print(emojis(message)) # daha sonra aldığımız veriyi kullanıp ekrana yazdırıyoruz
