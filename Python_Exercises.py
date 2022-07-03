
# Aşağıda verilen değişkenlerin tipini yazdırınız.

x = 10
y = 3.14
z = 3j + 10
k = " Hello AI "
j = False
a = 32 < 35
b= [2,3,4,5]
d= {"Name": "Zeynep",
    "Surname": "Azili",
    "Address": "Istanbul",
    "Age": 37}
t = ("Data Science","Machine Learning","Deep Learning")
s = {"Data Science","Machine Learning","Deep Learning"}


type(x)
type(y)
type(z)
type(k)
type(j)
type(a)
type(b)
type(d)
type(t)
type(s)

# Built-in functions in python

dir(d)  # Nesnelerin niteliklerini içeren bir liste verir.
['__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',]

help(list) # Herhangi bir nesne hakkında bilgi almak için kullanılır.

print(*enumerate("zeynep")) #her bir karaktere numaralandırma yapar.
# (0, 'z') (1, 'e') (2, 'y') (3, 'n') (4, 'e') (5, 'p')

print("Zeynep") # Çıktı olarak ifadeyi ekrana bastırır.
# Zeynep


# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space(boşluk) koyunuz, kelime kelime ayırınız.

text = "Keep your eyes on the stars,and your feet on the ground."
dir(text)
text=text.upper()
text=text.replace(","," ")
text=text.replace("."," ")
text=text.split()
text


""" Ya da """

text.upper().replace(","," ").replace("."," ").split()

# Verilen listeye aşağıdaki methodları uygulayınız.

list = ["V","E","R","I","B","I","L","I","M","I"]
dir(list)
list.sort()
# ['B', 'E', 'I', 'I', 'I', 'I', 'L', 'M', 'R', 'V']
list.pop(5)
# 'I' , listenin 5. indexini siler.
list.reverse()
# ['I', 'M', 'I', 'L', 'I', 'B', 'I', 'R', 'E', 'V']
len(list)
# 10; listenin eleman sayısı

# Verilen liste üzerinden ["V", "E", "R", "I"] listesi oluşturunuz.
list[0:4]
# Listenin son elemanı nedir?
list[-1]
# Yeni bir eleman ekleyiniz.
list.append("N")
# ['V', 'E', 'R', 'I', 'B', 'I', 'L', 'I', 'M', 'I', 'N']
# Sekizinci indekse "N" elemanını ekleyiniz.
list.insert(8,"N")

## Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Ahmet': ["Afrika",18],
        'Ayse':["Uganda",12],
        'Salih':["Ozbekistan",22],
        'Davud':["Cezayir",25] }

dict.keys()
# dict_keys(['Ahmet', 'Ayse', 'Salih', 'Davud'])
dict.values()
# dict_values([['Afrika', 18], ['Uganda', 12], ['Ozbekistan', 22], ['Cezayir', 25]])


# Key değeri "Fatma" value değeri ["Türkiye",24] olan yeni bir değeri ekleyiniz.

dict["Fatma"] = ["Türkiye",24]
dict
# Key değeri "Ayse" olan kişinin yaşını 15 olarak güncelleyiniz.
dict["Ayse"][1] = 15
dict
# ya da
dict.update({"Ayse": ["Azerbaycan",15]})
dict

# "Salih" i sözlükten siliniz.
dict.pop("Salih")
dict
dir(dict)

# Aşağıda verilen listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve
# bu listeleri gösteren bir fonksiyon yazınız.

s=[4,11,26,97,20,38]

def func(x):
     even_list = []
     odd_list = []

     for i in x:
          if i%2==0:
               even_list.append(i)
          else:
               odd_list.append(i)

     return even_list,odd_list

even_list,odd_list = func(s)

even_list
odd_list
func(s)
