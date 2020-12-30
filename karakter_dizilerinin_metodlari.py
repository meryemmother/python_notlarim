"""
replace()
metodu kullanarak bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirebiliriz.
"""
x="meryem"
print(x.replace("e","E"))
print(x.replace("e", ""))
print(x.replace("e", "", 1))


"""
split(), rsplit(), splitlines()
plit kelimesi Türkçede ‘bölmek, ayırmak’ gibi anlamlara gelir.
uygulandığı karakter dizilerini parçalarına ayırır.Örneğin:
"""
x = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")
for i in x.split():
    print(i[0], end="")
print()

y = "laleler"
for d in y.split("l"):
    print(d, end="")


"""
rsplit() metodunun ise sağdan sola doğru okumasıdır.
splitlines() metodunu ise bir karakter dizisini satır satır ayırmak için kullanabiliriz. 
"""

#lower()
#küçük harfe çevirmek için kullanırız.
print()
m = "MERYEM"
print(m.lower())


#upper()
#harfleri büyütmemizi sağlar.
print()
c = "meryem"
print(c.upper())



#endswith()
#karakter dizisinin hangi karakter dizisi ile bittiğini sorgulayabiliyoruz.
print()
ç = "meryem"
print(ç.endswith(b))


#startswith
#Bu metot, biraz önce gördüğümüz endswith() metodunun yaptığı işin tam tersini yapar.


