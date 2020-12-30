#Dictionaries değişstirebilir ve süslü parantezle ifade edilir. İndex yerine key ve value yani anahtar ve değer
#sistemi vardır yani değerlere anahtarla erişebiliriz.
dic = {
    "ısım": "İçimizdeki Şeytan",
    "Yazar": "Sabahattin Ali",
    "Dıl": "İngizlice"
}
print(dic)



#Bir değeri değiştirmek istediğimizde yine anahtar ile erişip değiştirebiliriz.
dic["Dıl"] = "Türkçe"
print(dic)


#Eleman eklemek için anahtar kullanırız.
dic["kıtap"]="Kürk Mantolu Madonna"
print(dic)

