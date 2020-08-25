# liste içindeki liste oluşturmaya 2d listeler denir
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][0]) # 4
matrix[1][0] = 15 # 1. indekse sahip listenin 0. öğesinin değerini değiştirdik
print(matrix[1][0]) # 15

# matrix değişkenin değerlerinin hepsini ekrana yazdır
for m in matrix:
    print(m)

# bu kodla matrix içindeki değerlerin hepsini yazdık fakat liste haline yazıldı
# peki ya liste içindeki listenin değerlerini nasıl yazdırabiliriz
# iç içe geçmiş for döngüsünden yararlanarak
for row in matrix:
    for item in row:
        print(item)
# iç içe geçmiş döngülerlerden yararlanarak tüm ögeleri tek tek yazdırabildik

