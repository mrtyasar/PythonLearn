for item in 'Python':
    print(item)

for item in ['murat','caner','ahmet']:
    print(item)

for item in [0,1,2,3,4,5,6,7,8,9]:
    print(item)

# bu listeyi şu şekilde yazmak yerine aralık vererek yazdırabiliriz
# bunun için range() fonksiyonunu kullanılırız
# parametre olarak verdiğimiz sayıya kadar sayıları barındırır
# fakat son parametreyi dahil etmez:
for item in range(1,10):
    print(item) # 1 2 3 4 5 6 7 8 9
# 10 a kadar git fakat 10 u dahil etme dedik bilgisayara

# eğer 0 dan başlatacaksak sayıları range fonksiyonuna sadece son sayıyı söyleyebiliriz
print('-------------')
for m in range(10):
    print(m)
print('--------------------')
# 3. bir parametre girerek kaçar kaçar gitmesini belirtebiliriz
for m in range(1,10,2): # 2 atlaya atlaya git
    print(m) # 1 3 5 7 9

# size bir liste verilecek bu liste alışverişte harcanan miktarın listesidir
# bu listedeki miktarları for döngüsü kurarak toplam maliyetini hesaplayınız:
prices = [10,20,30] # alışveriş listesi
total = 0 # toplamını saklayacağımız yer
for price in prices: # prices teki her bir ögeye price adını vererek:
    total += price # her bir price ögesini total değişkenine ekle
print(f'Total: {total}') # toplam masrafı yazdır dedik