# :) :( gibi işaretleri emoji hallerine çeviriecek bir program yazalım
message = input('> ')
words = message.split()
emojis = {
    ':)':'😁',
    ':(':'😢'
}
output = ''
for word in words:
    output += emojis.get(word,word) + ' '
print(output)