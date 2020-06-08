dersler= {"mete" : ["Veritabanları" , "işletim sistemleri"], "oğuz": ["java","php"], "kerem": ["linear algebra","math"]}

mete= {1,2,3}
ahmet=(1,2,3,4)
aaa=[1,2,3,4]
print(type(mete),type(ahmet),type(aaa))





print(type(dersler))

print(dersler["mete"])

for i in dersler.items():
    print(i)
'''
for i,j in dersler.items():
    print(i + "derslerini aldı: "+ j)

'''

for i in dersler.items():
    print(type(i))
    print(i[0] ,i[1])




isim=input("isim giriniz")

print(" {} in aldığı dersler:".format(isim))

for i in (dersler[isim]):
    print(i)



print(dersler["mete"])

