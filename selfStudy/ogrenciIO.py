
## python calisan arkadaslar icin bir ogrenci uygulaması yazdım
## dosyaya ogrenci ekleyen ogrenci silen ve goruntuleyen bir uygulama
## merak edenler bakabilirler


import os

dizi = ["ad", "soyad", "yas", "okul", "bolum"]
index = 0
devam = True


def ara(dict, katar):
    global dizi
    global devam
    global index

    if index == len(katar):
        index = 0
        return devam

    if dict[dizi[index]] == katar[index] or dict[dizi[index]] == "":
        # print("yazi :",dict[dizi[index]],katar[index] , index)
        index += 1
        devam = ara(dict, katar)
    else:
        devam = False

    return devam


def bilgiDoldur():
    dict = {}
    print("warning :girmek istemediginiz bilgileri bos birakin")
    ad = input("ogrenci adi ...:")
    soyad = input("ogrenci soyadi ....:")
    yas = input("ogrenci yasi....:")
    okul = input("ogrenci okulu ....:")
    bolum = input("ogrenci bolumu....:")

    if ad == "" and soyad == "" and yas == "" and okul == "" and bolum == "":
        print("\nErr :Lutfen en az 1 deger giriniz")
    else:

        if (ad != ""):
            dict["ad"] = ad
        else:
            dict["ad"] = ""

        if (soyad != ""):
            dict["soyad"] = soyad
        else:
            dict["soyad"] = ""

        if (yas != ""):
            dict["yas"] = yas
        else:
            dict["yas"] = ""

        if (okul != ""):
            dict["okul"] = okul
        else:
            dict["okul"] = ""

        if (bolum != ""):
            dict["bolum"] = bolum
        else:
            dict["bolum"] = ""

    return dict


def goruntule(katar):
    if sonuc == True:
        print("Success.....:")
        print("ad :", katar[0])
        print("soyad :", katar[1])
        print("yas :", katar[2])
        print("okul :", katar[3])
        print("bolum :", katar[4])
    devam = True  # devami en sonda true yaptik


def dosyaAc(fileName, mode):
    try:
        dosya = open(fileName, mode)
    except:
        print("boyle bir dosya bulunmamaktatir...")
        return False
    return dosya


while True:
    print("-----------Yurt Otomasyonou ------------\n")

    print("1-Ogrenci Ekle")
    print("2-Ogrenci Sil")
    print("3-Ogrenci Listele")
    print("4-exit")

    var = int(input("secim....:"))

    if var == 1:
        dosya = open("ogrenciler.txt", "a+")  # sonuna ekle yoksa olustur oku/yaz
        ad = input("ad :")
        soyad = input("soyad :")
        yas = input("yas :")
        okul = input("okul :")
        bolum = input("bolum :")
        dosya.write(ad + "\t" + soyad + "\t" + yas + "\t" + okul + "\t" + bolum + "\n")
        dosya.close()
        print("ogrenci kayit edildi...")

    elif var == 2:

        dosya = dosyaAc("ogrenciler.txt", "r")
        if dosya == False: continue

        dosya2 = dosyaAc("ogrenciler2.txt", "a+")
        if dosya == False: continue

        dict = bilgiDoldur()
        if len(dict) == 0: continue

        while True:
            katar = dosya.readline()
            if katar == "": break

            # satiri dizi haline getiriyoruz
            katar = katar.split('\t')
            #

            # aramaya basliyoruz
            sonuc = ara(dict, katar)
            devam = True
            if sonuc == False:
                dosya2.write(katar[0] + "\t" + katar[1] + "\t" + katar[2] + "\t" + katar[3] + "\t" + katar[4])
            else:
                continue

        dosya.close()
        dosya2.close()

        os.remove("ogrenciler.txt")
        os.rename("ogrenciler2.txt", "ogrenciler.txt")




    elif var == 3:

        dosya = dosyaAc("ogrenciler.txt", "r")
        if dosya == False: continue

        boolean = input("ogrenci bilgisini girecek misiniz e/h ? :")
        # print("debug ....:",boolean)

        if boolean == "e" or boolean == "E":

            dict = bilgiDoldur()

            if len(dict) == 0: continue
            while True:
                katar = dosya.readline()
                if katar == "": break

                # satiri dizi haline getiriyoruz
                katar = katar.split('\t')
                #

                # aramaya basliyoruz
                sonuc = ara(dict, katar)
                if sonuc == False:
                    continue
                else:
                    goruntule(katar)

            if sonuc == False: print("\nNo result...\n")

        else:
            print("--------------------------\n")
            ogrenciler = dosya.read()
            print(ogrenciler)
            print("---------Dosya Sonu ---------")

    elif var == 4:
        break
    else:
        print("yanlis deger girildi...\n")

    input()  # bos bekle
    os.system("cls")  # clear screen