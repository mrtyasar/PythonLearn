# Fonksiyonlar kodları içinde barındırarak belli işleri başka satırlarda daha kolay
# kullanabilmemizi sağlar

# selamlama fonksiyonunu yazalım

def selamlama():
    print('Selamlar!')
    print('Hoşgeldin sanal dünyaya!')

print('Start!')
selamlama()
print('Finish!')

# görsel emojilere dönüştüren fonksiyon yazalım

def emojiler():
    message = input('> ')
    words = message.split()
    emojis = {
        ':)':'😊',
        ':(':'😢'
    }
    output = ''
    for word in words:
        output += emojis.get(word,word) + ' '
    print(output)


print('Lütfen ruh halinizi yazınız:')
emojiler()