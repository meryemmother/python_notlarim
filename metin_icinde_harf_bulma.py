metin = """Öğrenmesi kolaydır. Çünkü basit bir yapısı ve tanımlanmış söz dizimi bulunuyor. Tabi buda Python dilini çabuk ve kolay bir şekilde öğrenmemizi sağlıyor.
Diğer programlara göre okunması basit bir programlama dilidir.
Kaynak kodu bakımı yönünden çok kolaydır.
Geniş bir kütüphaneye sahip olan Python, çapraz platform uyumlu olaması ile birlikte Windows, UNIX ve Macintosh gibi sistemlere kolay taşınabilir.
Python tüm platformlarda aynı arabirime sahip bir programlama dilidir. Ayrıca birçok donanım platformlarında kullanılabilir.
Python yorumlayıcı ya alt düzey modüllerini ekleyebilirsiniz. Ayrıca bu modüller, programcıların araçları için daha performanslı çalışması için yenilemesine imkan verir.
Python programlama dili birçok önemli ticari veritabanlarına bağlantı inşa edebilir.
Zamanlı çöp toplama özelliği bulunuyor.
Yüksek seviyede dinamik veri türleri sunar. Ayrıca dinamik tür denetimini inşa eder.
C, C++, ActiveX ve Java ile kolayca bağlantı oluşturulabilir."""

harf = input("Sorgulamak istediğiniz harf: ")

sayı = 0

for s in metin:
    if harf == s:
        sayı += 1

print(sayı)