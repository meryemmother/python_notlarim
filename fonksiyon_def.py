# def özel kelimesi Python'da fonksiyon tanımlamak için kullanılıyor.
# Sonra parametreleri belireniyor.
# Fazla parametre kullanmamız gereken durumlarda  "," yardımı ile belirtebiliriz.
#Return bölümünü ifade ediyoruz.


#def sayinin_karesi (sayi):
    #karesi = sayi * sayi
   # return karesi


#sayi= int(input("Karesini almak istedğiniz sayıyı giriniz:" ))

#karesi = sayinin_karesi(sayi)

#print(karesi)

#biraz daha kompleks bir örnek yapalım:

sayi1= int(input("Bölmek isyediğiniz sayıyı giriniz:" ))
sayi2= int(input("Bölmek istediğiniz diğer sayıyı giriniz:" ))


def bölme(sayi1, sayi2):
    if sayi1 == 0 or sayi2 == 0:
        print("Sıfır ile bölünemez.")
        return 0, 0
    bölüm = sayi1 / sayi2
    kalan = sayi1 % sayi2

    return bölüm, kalan

bölüm, kalan = bölme(sayi1, sayi2)
print("Bölüm ={} ,Kalan ={}".format(bölüm,kalan))



