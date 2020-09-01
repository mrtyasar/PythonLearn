from pathlib import Path

path = Path('ecommerce')
# exists() kullanarak böyle bir yolun olup olmadığını boolean değerinde öğreniriz
print(path.exists()) # True

# mkdir() işlevini kullanarak yeni bir yol yaratabiliriz
path = Path('ecommerce')
#print(path.mkdir())

# veya rmdir() işlevini kullanarak silebiliriz
path = Path('emails')
#print(path.mkdir()) # oluşturduktan sonra yorum satırı yapın yoksa hata alınıyor tekrar oluşturmaktan

# print(path.rmdir()) # ve bu kodları da

# glob() işlevi sayesinde uzantı girerek sınıfları dosyaları bulabiliyoruz
# glob() fonksiyonunu for döngüsü ile kullanırız

path = Path()
for file in path.glob('*'):
    print(file)





