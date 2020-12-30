#string kelimeleri hatta cümleleri kullanılan bir veri yapısı.
# #Stringler de listelerin çoğu fonksyionunu kullanabiliyoruz.büyük ya da küçük harfe döndürebilmemize
# olanak sağlayan lower() ya da upper() gibi fonksiyonları bulunuyor.
a = "Hello, World!"
print(type(a))
print(a.lower())

b="hello,world!"
print(type(b))
print(b.upper())

#Stringler üzerinde replace() metodu ile belirli
# bir karakteri ya da karakterleri başka bir karakter ya da karakterler ile değiştirebiliyoruz.
print(a.replace("Hello" , "hi"))

#Stringleri listelerde olduğu gibi bölebiliyoruz.
print(a[0:3])

#split() isimli  fonksyion ile belirli karakterlere göred bölebiliriz.
a=("hello, world")
a.split(" o ")


#Stringler ile + operatörü ile stringleri birbirlerine ekleyebiliriz.
ulke="Türkiye"
print("Burası "+ulke+"")

