def yazdir():
    isim="elif"
    print("ismin: ",isim)
yazdir()

print("*********")
def isimYazdir(ad):
    print("hello and welcome python course ",ad)
ad="Elif"
isimYazdir(ad)

print("***********")
def metot(sayi=7):
    print("sayı: ",sayi)
metot(6)
metot()

print("***********")

def tahmin():
    global rakam
    rakam=7
    return rakam
rakam=9
print(tahmin())
# return
meslekAdi=" "
def name(meslekAdi):
    meslekAdi=input("meslek adı giriniz:")
    return meslekAdi
print("meslek adı: ",name(meslekAdi))

print("*********")
# args kullandığımızda istediğim kadar parametere girip metodu kullanabilirim
def agsMetot(*args):
    return sum(args)
b=agsMetot(23,44,56,7,4,3,6,8,6)
print("sayıların toplamı: ",b)

print("***********")
# kwargs dictionary yapıyor
def kwargsMetot(**kwargs):
    print(kwargs)
kwargsMetot(üzüm=23,kayısı=44)

# HAZIR METOTLAR

#MAP

listem=[2,8,9,4,6,7,8,99,100]
def listeYazdir(sayi):
    return sayi/2
print(list(map(listeYazdir,listem)))

# FİLTER
def controlString(string):
    return "Elif" in string # Elif Duman ın içide Elif kelimesi geçiyor mu onu kontrol eder geçerse true,geçmezse false değer döndürür
print(controlString("Elif Duman")) 

listem2=["Elif","Elif Duman","Duman","Berfin"]
print(list(map(controlString,listem2))) # map kullanarak
print(list(filter(controlString,listem2))) # filter metoduyla içinde sadece Elif kelimesi geçenleri listeye atıyor

def  tekSayiBulma(sayi):
    if(sayi%2==1):
        return sayi
listem3=range(1,21)
print(list(filter(tekSayiBulma,listem3))) # tek sayıları filtreleyip yazar

# LAMBDA
fonksiyon=lambda num:num*3 # def fonksiyonu kullanmadan yapılır
print(fonksiyon(20))
print(list(map(lambda k:k/2,listem)))
