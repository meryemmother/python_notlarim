#Bir listede bulunan her elemanın üzerinde teker teker işlem ve filtreleme yapmamızı sağlar ve
#tüm bu çıktıları tekrar bir listeye koyar.

#Örneğin bir listeden yalnızca tek sayılardan oluşan bir liste oluşturalım.

liste = list(range(100))
tek_sayılar = []
for i in liste:
    if i % 2 != 0:
        tek_sayılar.append(i**2)
print(tek_sayılar)
#List comprehensions ile yapalım
liste = list(range(100))
print([i**2 for i in liste if i %2 !=0])