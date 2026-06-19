#TRY - EXCEPT
while(True):
    try:
        yas=int(input("yaş giriniz: "))
        print("iki katı:  ",yas*2)
        break
    except ValueError:
        print("yanlış girdiniz:")
    else:
        print("bu kısım çalışmaz try ve except in dışına çıkamadık")
    finally:
        print("bu kısım hep çalışır")  

print("***********")

#TYPE ANOTATİON
isim:str="Elif"
print(type(isim))
age:int=22
ogrenciMi:bool=True
def add_numbers(a:int,b:int):
    return a+b
print(add_numbers(8,8))

def metot(value:int|str):
    if(isinstance(value,int)):
        return f"integer: {value}"
    else:
        return f"string: {value}"
print(metot(45))
print(metot("Elif"))
import numpy # numpy modülü
print((numpy.zeros((3,5))))