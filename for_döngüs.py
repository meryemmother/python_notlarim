#Python'da For döngülerinin asıl amacı bir obje üzerinde tek tek gezinmek.
#istediğimiz sayıda tekrar eden döngüler oluşturabiliyoruz.
#amacımız döngünün 10 kez dönmesi ise 10 elemana sahip bir liste oluşturur
# For ile liste üzerinde geziniriz böylece döngü 10 kez tekrar eder.

for i in range(20):
    print(i)

# Örneğin 5' dan 20'e kadar 3er 3er giden bir liste yapmak için
print(list(range(5,20, 3)))

#listenin uzunluğunu almak için;
liste = (2,4,6,8,)
for i in range(len(liste)):
    print(i)
#enumerate ile  liste üzerinde For ile gezinirken index numarasını da alabiliyoruz.
for index, i in enumerate(liste):
    print("index =", index, "/ iterator =", i)


#break ile döngüyü kırıyoruz Continue ise döngüyü kırmıyor ancak döngüyü atlatıyor.

for i in range(5):
    if i == 3:
        continue
    print(i)
#burda üçü basmadık.


#Eğer sayıları hem tersten, hem de mesela 3’er 3’er atlayarak yazmak istersek:
for i in range(10, 0, -3):
    print(i)
