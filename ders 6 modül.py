import tuple # böyle yaparak tuple adında oluşturduğum dosyadaki listem verisini alabiliyoruz
print(tuple.listem)

# RANDOM MODÜLÜ
import random
a=random.random()  # 0-1 arasından float bir değer döndürür
print(a)
b=random.uniform(1,50) # 1-50 arasından float bir değer döndürür
print(b)
c=random.randint(1,50) # 1-50 arasından int bir değer döndürür
print(c)

# MATH MODÜLÜÜ
import math
d=math.factorial(5)
print("sonuç: ",d)
e=math.pow(3,4)
print(e)
f=math.pi # pi sayısının değerini yazdırır
print(f)
g=math.sqrt(100)
print(g)
h=math.floor(3.8)
print(3.8," sayısının kendisinden küçük en büyük tam sayıya yuvarlar ve o sayı: ",h)

# TİME MODÜLÜ
import time
print(time.gmtime())
print(time.localtime())
print(time.asctime())

