# SET
liste=[12,3,2,1,5,7,12,9,0,7,6,4,4] # set tekrarlayan elemanları yazmaz ayrıca sıralı olarak yazar
setim=set(liste)
print(len(setim))
print(setim)
#setim.add(23)
#print(setim)
setim2=[23,45,6,7,99,0]
print(setim.union(setim2)) # setleri birleştirme
print(setim.intersection(setim2)) # setlerin kesişimini bulma
bosSet=set() # boş set böyle oluşturulur
print(bosSet)
print(type(bosSet))
bosSet.add(12)
bosSet.add(14)
bosSet.add(12)
print(bosSet) # 12'yi bir kez yazdırır


