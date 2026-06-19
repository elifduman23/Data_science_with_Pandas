# AND - OR
"""x=7
y=9
z=5
print(x<y and z<x)
print(y<x or z<y)"""
print(not 1==1) # not tersine çevirir
dict ={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}
print(5 in dict.values())

#İF ELİF ELSE
yas=int(input("yaşınızı giriniz:"))
if(yas<18):
    print("çocuk")
elif(yas>=18 and yas<30):
    print("yetişkin")
elif(yas>=30):
    print("yaşlı")
else:
    print("doğru bilgi giriniz")
   

# DÖNGÜLER
listem=[1,2,3,45,6,7,8,3,2,44]
for k in listem:
    print(k*5)
print("döngü bitti")

for e in listem:
    if(e %6==0):
        print(e)
print("döngü bitti")

listen2=[("a","b"),("c","d"),("e","f")]
for (x,y) in listen2:
    print(y)

sozluk={"a":1,"b":2}
for (key,value) in sozluk.items():
    print(value)
print("***********************")

# CONTİNUE BREAK 
for d in listem:
    if (d==3):
        print("döngü durduruldu")
        break
    print(d)

for d in listem:
    if(d%2==0):
        continue
    else:
        print(d)

print("**********************")

# WHİLE DÖNGÜSÜ

x=0
while x<10:
    print(x)
    x+=1


