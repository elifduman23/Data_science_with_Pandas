import numpy as np
import math
 # numpy kütüphanesini kullanmamızı sağlar
#NUMPY KÜTÜPHANESİ:
listem=[1,2,3,4]
my_numpy_array=np.array(listem)
print(my_numpy_array)
print(type(my_numpy_array))
print(my_numpy_array.max())
print(np.zeros(5)) # 5 tane 0'dan oluşan numpy dizisi
print(np.ones(10)) # 10 tane 1'den oluşan numpy dizisi
print(np.random.random(3)) # 3 adet 0-1 arasında random sayı üretir
listem2=[5,6,7,8]
my_numpy_array2=np.array(listem)
my_numpy_array3=np.array(listem2)
print(my_numpy_array2+my_numpy_array3) # listelerdeki 1-5,2-6,3-7,4-8 değerlerini toplar,bu işlemlerde iki dizinin boyutu aynı olmalıdır
print(my_numpy_array2*2) # listemdeki değerleri numpy dizisine çevirir daha sonra elemanları tek tek 2 ile çarpar
print(np.arange(0,10)) # listelerde olduğu gibi burdada 0-10 arasında oluşturabiliyoruz
print(np.arange(0,20,3))
np_array=np.arange(0,92)
print(np_array[0]) # yine liste mantığıyla aynıdır
print(np_array[-1]) # son elemanı gösterir
print(np_array[1:4:])
print(np_array[::-1])
print(np.random.randint(1,100,9)) # 1-100 arasında rastgele 9 adet tamsayı verir
my_matrix=[[2,3],[6,0]]
print(np.array(my_matrix))
print(my_matrix[0]) # [2,3] 'ü verir
print(my_matrix[1][0]) # 6'yı verir
matrix1=np.array([[4,4],[9,1]])
print(matrix1.sum()) # matristeki elemanları toplar
print(matrix1[1][0])
print(np.ones((9,9)))
print(np.random.random((4,5)))
print(np.random.randint(0,100,(3,2)))
print("matris toplamı:")
first_array=np.array([[5,10],[15,20]])
second_array=np.array([[25,30],[35,40]])
print(first_array+second_array)
third_array=np.array([10,20]) 
print(second_array+third_array) # 25-10,30-20,35-10,40-20 değerlerini toplar
fourth_array=np.array([[30],[40]])
print(first_array+fourth_array) # böyle toplayabilir
print("matrix çarpımı")
print(first_array*second_array)
print(first_array.shape) # matris boyutunu gösterir
# .dot metot
matrix2=np.array([[2],[4]])
print("1.matris")
print(matrix2)
print("matris2 büyüklüğü: ",matrix2.shape)
matrix3=np.array([[2,3,4]])
print("2.matris")
print(matrix3)
print("matris3 büyüklüğü: ",matrix3.shape)
print("sonuçları")
sonuc_matrix=matrix2.dot(matrix3)
print(sonuc_matrix)
print("oluşan yeni matrisin büyüklüğü: ",sonuc_matrix.shape)
print("**************")

matrix_array=np.random.randint(1,100,20)
print(matrix_array)
print(matrix_array[matrix_array>50]) # 50 'den büyük olanları yazdırır
# transpoze
print(matrix1.transpose()) # transpoze edilmiş matris
print(matrix1.T) # bu şekilde de olabilir
yeni_matrix=np.array([[1,2,5],[4,7,6]])
print("yeni_matrix'in büyüklüğü: ",yeni_matrix.shape)
transpose_matrix=yeni_matrix.T
print(transpose_matrix)
print("Transpose edilmiş matrix'in büyüklüğü: ",transpose_matrix.shape)
#reshape ile istediğimiz büyüklükte yapabiliriz
print(yeni_matrix.reshape(3,2))
data=np.array([23,44,60,6,25,58,35,34])
ortalama=np.mean(data)
print("ortalama: ",ortalama)
toplam=np.sum(data)
print("toplam: ",toplam)
standart_sapma=np.std(data)
print("standart sapma: ",standart_sapma)
zscores=(data-ortalama)/standart_sapma
print(zscores)
print(zscores[zscores>1])
print(data[zscores>1])
print("*************")
print("math equations")
# 2x+3y=8 and 5x+7y=19 x,y=?
A=np.array([[2,3],[5,7]])
b=np.array([8,19])
print(np.linalg.solve(A,b)) # denklemin sonucunu bulur

print("***********")

print("KENDİ KENDİME ALIŞTIRMALAR:")
new_array=np.array([[1,2],[9,9],[6,0]])
new_array2=np.array([[6,0,1],[9,9,2]])
new_matrix=new_array.dot(new_array2)
print(new_matrix)
print("oluşan yeni matrsin büyüklüğü: ",new_matrix.shape)
print("transpoze etme: ",new_matrix.T)
print("yeni boyut: ",new_matrix.reshape(9,1))
print("yeni boyut: ",new_matrix.reshape(1,9))
print("7x+9y=19,6x-2y=8")
np_arry=np.array([[7,9],[6,-2]])
np_arry2=np.array([19,8])
print("sonuç: ",np.linalg.solve(np_arry,np_arry2))

