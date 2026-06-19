 # SÖZLÜKLER
meyve=["muz","elma"]
kalori=[100,50]
fitness={"muz":100,"elma":50}
print(type(fitness))
print(fitness["elma"])
print(fitness.keys()) # anaharları keys alır
print(fitness.values()) # değer values alır
fitness["elma"]=150
print(fitness.values())
fitness["kavun"]=120
print(fitness)
print(fitness.get("erik",0)) # dictionary içinde erik key ine sahip bir kelime var mı diye bakar eğer yoksa 0 döndürür
print(fitness.get("elma",0)) # elma dictionary ide olduğundan elmanın value değerini döndürür

sozlugum={23:"merve",44:"elif"}
print(sozlugum)
karisik={"1":100,"2":12.44,"3":[23,60]} # böyle karışık veri türlerini de bulundurabilir
print(karisik["3"][1]) # dictionarinin içideki lstede bulunan 60 değerini yazdırır
enKarisik={"k1":10,"k2":[23,44,12],"k3":"meryem","k4":{12:"kedi",13:"köpek"}}
print(enKarisik["k4"][12]) #dictionary içide olan dictionary nin içinde olan kedi değerini ekrana yazdırır
print(enKarisik["k2"][2]) # dictionaryinin içinde olan listede olan 12 yi yazdırır


