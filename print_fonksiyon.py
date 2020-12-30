#print fonksiyonu parametreeri:

#SEP parametresinin öntanımlı değerinin bir adet boşluk varıdr.
# Yani aslında Python yukarıdaki ilk komutu şöyle görüyor:
print(*"Galatasaray", sep=" ")
#dizisinin her bir öğesinin
#arasına bir adet boşluk karakteri yerleştiriliyor.Bunu çeşitli şekillerde kullanabilirz
# her öğenin arasındaki boşluğu silme veya başka şekillerde örnek:
print(*"GALATASARAY", sep="-")


#TERS TAKSİM
#Eğer ters taksim kullanarak enter tuşuna
#basmadan önce bu işareti kullanırsak Python tıpkı üç tırnak işaretlerinde şahit olduğumuz
#gibi, hata vermeden bir alt satıra geçecektir.örnek
print("Bu gün python 3 kitabının\
 ters taksim bölümüne gelmiş bulunmaktayım\
 burada öğrendiklerimi notlar alıyorum.")

