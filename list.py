#list çok değişkenli yapılardır.Listelerdeki her değişkenin kendine ait indexi vardır,0dan başlar.
liste=["elma","armut","çilek","muz","erik"]
print(liste[0])


#Listenin uzunluğunu .len methodu kullanırız.
liste=["elma","armut","çilek","muz","erik"]
print(len(liste))

#append() fonksiyonu ile  listenin sonuna eleman ekleyebiliriz.
liste=["elma","armut","çilek","muz","erik"]
liste.append("karpuz")
print(liste)


#listenin istediğimiz yerine değişken eklemek için insert() fonksiyonunu kullanabiliriz.
liste=["elma","armut","çilek","muz","erik"]
liste.insert(2,"kiraz")
print(liste)

#Eleman silmek için remove()' u kullanabiliriz.
#Sıralamak için sort()' u kullanabiliriz.


#listeleri bölmek için çin köşeli parantezler içerisinde ki lokasyon yapısına : ekliyoruz.
# 0. index ile başla ve 2.index'e kadar(dahil değil) al(döndür).
liste=["elma","armut","çilek","muz","erik"]
print(liste)
print(liste[0:2])

#son elemana kadar git demek için ise (liste[1:]) yapabiliyoruz.

#Sıralamak için sort()' u kullanabiliriz.
