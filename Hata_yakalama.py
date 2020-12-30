"""
try… except
hata yakalama işlemleri için try... except... bloklarından yararlanılır.öRNEK:
except ValueError:
print("Lütfen sadece sayı girin!")
try… except… as…
hata açıklaması var.
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError as hata:
    print("Sadece sayı girin!")
    print("orijinal hata mesajı: ", hata)


raise
programda, kullanıcının yaptığı bir işlem normal şartlar altında
hata vermeyecek olsa bile biz ona ‘Python tarzı’ bir hata mesajı göstermek isteyebiliriz.
Böyle bir durumda  raise kullanırız.
örnek:
bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

bölen = int(input("bölen sayı: "))
print(bölünen/bölen)
"""




