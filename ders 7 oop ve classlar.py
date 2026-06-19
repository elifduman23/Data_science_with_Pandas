class Person():
    name=" "
    age=0
    def __init__(self,nameInput,ageInput):
        print("init metodu çalıştırıldı")
        self.name=nameInput
        self.age=ageInput
kisi1=Person("barış",25)
print(type(kisi1))
#kisi1.name="barış"
print(kisi1.name)
#kisi1.age=25
print(kisi1.age)
kisi2=Person("elif",21)
print(kisi2.name)
print(kisi2.age)

print("***********")
class Bilgiler():
    # numara ,ad ,soyad değişkenlerini tanımlamasak da olur 
    def __init__(self,numara,ad,soyad):
        self.numara=numara
        self.ad=ad
        self.soyad=soyad
    def yazdir(self): # burda self kullanımı zorunludur
        print(self.ad)
        print("yazdırıldı")
kisi3=Bilgiler(2,"Yaren","Ocakcıbaşı")
kisi3.yazdir()
print(kisi3.numara)
print(kisi3.ad)
print(kisi3.soyad)

print("**********")
"""class Dog():
    year=7
    def __init__(self,age):
        self.age=age
    def humanAge(self):
        return self.age*self.year # self.year yerine Dog.year da yazabiliriz
kopek=Dog(3)
print(kopek.age)
yas=kopek.humanAge()
print(yas)"""

class Dog():
    year=7
    def __init__(self,age=4):
        self.age=age
        self.yas=age*self.year
        print("oluşturuldu")
    def humanAge(self):
        return self.age*Dog.year
kopek=Dog()
print(kopek.age)
print(kopek.humanAge())