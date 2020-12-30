kullanici_adi = input("Kullanıcı adınızı giriniz:")
parola = input("Parolanızı giriniz:")
toplam_uzunluk = len(kullanici_adi)+len(parola)
print("Kullanıcı adı ve paralonızın toplam uzunluğu:{}".format(toplam_uzunluk))
if toplam_uzunluk >= 40:
    print("Kullancı adı ve parolanız '40' karekterden uzun olmamalıdır.")
else:
    print("Sisteme hoşgeldiniz")
