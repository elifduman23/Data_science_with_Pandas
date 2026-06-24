import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None) # tüm kolonları gösterir
pd.set_option('display.max_rows', None) # tüm satırları gösterir
data=pd.read_csv("titanic.csv") 
names=data["Name"]
print(names)# yolcuların adlarını verir

