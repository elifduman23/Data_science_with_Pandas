# İNHERİTANCE
class Musician():
    def __init__(self,name):
        self.name=name
        print("musician class")
    def test1(self):
        print("test1")
    def test2(self):
        print("test2")
kisi1=Musician("Elif")
print(kisi1.name)
kisi1.test1()
kisi1.test2()
class MusicianPlus(Musician): # musicianPlus musician class ından miras aldı
    def __init__(self,name):
        Musician.__init__(self,name)
        print("musician plus")
    def test1(self):
        print("test1 değiştirildi")
kisi2=MusicianPlus("emir")
print(kisi2.name)
kisi2.test1()
kisi2.test2()

print("*******************")
#POLİMORFİZM
class Banana():
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"100 kalori {self.name}"
    
class Apple():
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"100 kalori {self.name}"

muz=Banana("muz")
elma=Apple("elma")
print(muz.info())
print(elma.info())
fruits=[muz,elma]
for k in fruits:
    print(k.info())

print("**********")
#ENCAPSULATİON
class Phone():
    def __init__(self,name,price):
        self.name=name
        self.__price=price # alt çizili olunca price kısmına dışarıdan erişime ve değiştirilmesine izin vermiyoruz
    def info(self):
        print(f"{self.name} price is: {self.__price}")
    def ChangePrice(self,price):
        self.__price=price
        print(f"{self.name} price is: {self.__price}") # eğer fiyatı metot içinde değiştirmek istiyorsak bu yolu uygulayabiliriz
iPhone=Phone("İphone 15 ProMax",880000)
iPhone.info()
iPhone.__price=75000 # yukarıda __price olduğundan fiyatı 75000 olarak değiştiremeyiz
iPhone.info()
iPhone.ChangePrice(75000) 

#ABSTRACTİON (SOYUTLAMA)

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def maxSpeed(self):
        pass

class Tesla(Car):
    def maxSpeed(self): # car sınıfını kullandığım için maxSpeed kısmunı yazmak zorundayız
        print("200km")
arabam=Tesla()
arabam.maxSpeed()

print("************")
class Fruit():
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories
    def __str__(self): # aşağıda yazdığım print(meyveler) kısmını yazdırır
        return f"{self.name}: {self.calories} calories"
    def __len__(self):
        return self.calories
meyveler=Fruit("erik",144)
print(meyveler)
print(len(meyveler))
        