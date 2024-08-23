print ("Projek Pengelolaan Kontak")

# Program Manajemen Kontak
import function_program2

# List of Dictionary
daftar_kontak = []
daftar_kontak.append ({
    "nama" : "rendy",
    "email" : "rendy123@gmail.com",
    "telepon" : "9873149810"
})

# Menu Program
while True :
    print ("# Menu")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Hapus Kontak")
    print ("4. Cari Kontak")
    print ("0. Keluar Program")

    menu = input ("Pilih Menu : ")

    if menu == "0" :
        break
    elif menu == "1" :
        function_program2.display_kontak (daftar_kontak)
    elif menu == "2" :
        kontak = function_program2.new_kontak ()
        daftar_kontak.append (kontak)
    elif menu == "3" :
        function_program2.hapus_kontak(daftar_kontak)
    elif menu == "4" :
        function_program2.cari_kontak(daftar_kontak)
    else :
        print ("Menu tidak tersedia")

print ("Program Selesai Berjalan, Sampai Jumpa")