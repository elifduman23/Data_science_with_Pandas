for k in list(range(0,10)):
    print(k)
print(list(range(5,25,2)))

print("************")
listem=[1,2,3,4,56,7,8,4,2,2,5,7,8,22,45,77,44,23]
for index in range(len(listem)):
    print(index) # indeks yazdırır

for k in enumerate(listem):
    print(k) # indeks ve value

for (index,value) in enumerate(listem):
    print(index)
print("*************")
print("oluşturulan random bir sayı:")
import random
print(random.randint(0,100))























