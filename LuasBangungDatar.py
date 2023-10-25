# Soal No 2 menghitung Luas Bangun Datar 

keterangan = '''Selamat Datang di aplikasi menghitung luas bangun datar
Masukan pilihan :
1 untuk menghitung luas persegi 
2 untuk menghitung luas lingkaran
3 untuk menghitung luas segitiga
silahkan pilih ?
'''
pilihan = input (keterangan)

match pilihan:
    case "1" :
        print ("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input ("masukan sisi ?"))
        LuasPersegi = sisi * sisi 
        print ("luas persegi adalah", LuasPersegi)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        r = int (input ("masukan jari-jari ?"))
        LuasLingkaran = 3.14 * r**2
        print ("Luas Lingkaran adalah", LuasLingkaran)
    case "3":
        print ("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input ("masukan alas ?"))
        tinggi = int(input ("masukan tinggi ?"))
        LuasSegitiga = 0.5 * alas * tinggi
        print ("Luas Segitiga adalah", LuasSegitiga)
    case _:
        print ("pilihan anda salah")
