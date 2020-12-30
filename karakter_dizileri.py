#for i in range kullanarak kullanıcadan gelecek olan belirsiz uzunluktaki dizinin
#öğelerine len fonksiyonu ile birlikte kolayca erişebiliyoruz.
isim = input("isminiz: ")

for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i, isim[i]))




#karakter dizilerini dilimlemek örneğin:
x = "2021 yılında bol bol ders çalış."
print(x[4:12])


#Karakter Dizilerini Ters Çevirmek
x = "2021 yılında bol bol ders çalış."
print(x[::-1])
#bunun yerine istersek reversed() adlı bir fonksiyondan da yararlanabiliriz.
print(*reversed("2021 yılında bol bol ders çalış."), sep="")



#Karakter Dizilerini Alfabe Sırasına Dizmek
#sorted() adlı bir fonksiyondan yararlanacağız:
print(*sorted("meryem"),sep="")
for i in sorted("kitap"):
    print(i,end="")



#Karakter dizileri üzerinde değişiklik yapmak:

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for i in site1, site2, site3, site4:
    print("http://", i, sep="")


#başka bir örnek
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler = []
sessizler = []
kelime ="meryem"
for i in kelime:
    if i in sesli_harfler:
     sesliler.append(i)
    else:
        sessizler.append(i)
sesliler = set(sesliler)
sessizler = set(sessizler)
print("Kelimedeki sesli harfler:", sesliler)
print("Kelimedeki sessiz harfler:", sessizler)





""""
dir()
Bu metot bize Python’daki bir nesnenin özellikleri hakkında bilgi edinme imkanı verecek.
Mesela karakter dizilerinin bize hangi metotları sunduğunu görmek için bu fonksiyonu şöyle kullanabiliriz:
"""
print(dir(str))




#enumerate()
#enumerate() fonksiyonu öğe ve bu öğeye ait bir sıra numarasını verir.
print(*enumerate("kalem"))







