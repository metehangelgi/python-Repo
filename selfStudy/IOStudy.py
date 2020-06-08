

try:
    dosya=open("testMe.txt","r")
    print(dosya.read())
    print(dosya.readline())
    print(dosya.readlines())
    dosya.close()
    with open("testMe.txt","r") as dosya:
        dosya.seek(10)
        print(dosya.read())
        print()
        dosya.seek(5)
        print(dosya.read(10))

    with open("testMe.txt","a") as dosya:
        dosya.write("\nkerem: biz biz biz")
        dosya.seek(0) #--- en başına gidiyor ve üstüne yazıyor
        dosya.write("\nmetehan: biz biz biz")
    with open("testMe.txt", "r+") as dosya:
        data=dosya.read()
        dosya.seek(0)
        data="sen biz siz karıştı \n"+data
        dosya.write(data)
    with open("testMe.txt","r+") as dosya:
        data=dosya.readlines()
        data.insert(2,"bu da son aşama olsun \n")
        dosya.seek(0)
        dosya.writelines(data)
    #open("testMe.txt", "w").close()


except(FileNotFoundError):
    print(" I couldn't find file what you want ")





doca=open("testMe.txt", "w") # böylle yapınca da direk diğerilerinin üzerine yszıyo o yüzden datayı al işle hepsini tekrar bas.
doca.write("ben metehan")
doca.close()




