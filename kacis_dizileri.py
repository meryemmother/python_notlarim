
#Zil Sesi (\a)
#\a !bip! benzeri bir zil sesi üretilmesini sağlayabilir:
print("\a")


#\r kaçış dizisinden sonra gelen bütün karakterler aynı satırın başa dönmesini sağlar.
print("Merhaba\rDünya")

#İmleç kaydırma \b
#\b kaçış dizisinin etkisiyle imleç bir karakter sola kayar.Örnek
print("Başka bir\b örnek verelim.")#burda r harfini silmiş oldu.


# Düşey Sekme (\v) her işletim sisteminde çalışmayabiliyor.
print("düşey\vsekme")


#Küçük Unicode (\u)
#E kod konumlarını temsil etmek için kullanılır
#Ancak \U ile gösterilen kod konumları u ile gösterilenlere göre biraz daha uzundur.
#Uzun Ad (\N)UNICODE sistemi ile ilgili bir başka kaçış dizisi de \N adlı kaçış dizisidir.
import unicodedata
unicodedata.name('m')


#Onaltılı Karakter (\x)
# onaltılı (hexadecimal) sayma sistemindeki bir sayının karakter karşılığını gösterebiliriz.

#\f
#Yeni bir sayfaya geçilmesini sağlar.Artık çok kullanılmamaktadır.

#r karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.






#\n parametresi ,bir alt satıra geçilmesini sağlıyor
print("ters slas n  parametresi \n bir alt satıra \n geçilmesini sağlıyor")
başlık = "PYTHON 3"
print(başlık, "\n", "*"*len(başlık))



# \t adlı kaçış dizisi, sanki Tab (sekme) tuşuna basılmış gibi bir
#etki oluşturur.Örnek:
print("Bu", "gün", "günlerden", "Pazartesi", sep="\t")



