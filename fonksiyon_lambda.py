#Tek satırda yazılabilne basit fonksiyonlardır.

#Bölme işleminden kalanı bulmak için bir fonksiyon oluşturalım:

mod = lambda sayi1 , sayi2 : sayi1 % sayi2
print(mod(11, 3))



#Çok büyük bir liste ile işlem yaparken her elemana aynı fonksiyonu uygulamak istersek,
#map() kullanırız .İki parametre alan map' ın ilk parametresi
#uygulanmak istenen fonksiyon kinci parametresi listemiz oluyor.
#Sonra döndürdüğü map objesini list ile listeye çevirerek her elemanına fonksiyon uygulanmış
# şekilde  listeyi elede edebiliyoruz.
#önce  map() kullanmadan yapalım:

liste = [1, 2, 3, 4, 5]
kareler = []
for i in liste:
    kareler.append(i ** 2)

print(kareler)

#şimdi lamba ve map kullanarak tek satırda yazalım:
print(list(map(lambda x: x**2, list(range(1,6)))))
print(list(map(lambda x: x**2, list(range(1,6)))))
print(list(map(lambda x: x**2, list(range(1,6)))))
