# Objek terbagi menjadi 3, yaitu ; tanpa return dan tanpa argumen, meenggunakan argumen, menggunakan return

class buah :

    jumlah = 0

    def __init__ (jenis, nama, warna, berat, harga) :
        jenis.nama = nama
        jenis.warna = warna
        jenis.berat = berat
        jenis.harga = harga
        buah.jumlah =+ 1

# method tanpa return, tanpa argumen
    def siapa (jenis) :
        print (f'buah ini bernama {jenis.nama}')

# method dengan argumen, tanpa return
    def beratUp (jenis, up) :
        jenis.berat += up 

# method dengan return
    def getBerat (jenis) :
        return jenis.berat
    

buah1 = buah ('semangka', 'merah', 4, 15000)
buah2 = buah ('pisang', 'kuning', 3, 20000)

buah1.siapa()
buah2.beratUp(6)

print (buah2.getBerat())