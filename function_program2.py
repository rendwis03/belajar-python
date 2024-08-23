# Program Management Kontak

# Daftar Kontak
def display_kontak (daftar_kontak) :
    for kontak in daftar_kontak :
        print ("===========================")
        print (f"Nama : {kontak['nama']}")
        print (f"Email : {kontak['email']}")
        print (f"Telepon : {kontak['telepon']}")

# Tambah Kontak
def new_kontak () :
    nama = input ("Nama : ")
    email = input ("Email : ")
    telepon = input ("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak 


# Hapus Kontak
def hapus_kontak (daftar_kontak) :
    telepon = input ("Nomor telepon yang akan dihapus : ") # Berdasarkan nomer telepon
    
    index = -1 # Untuk menandai data yang tidak ketemu

    for i in range (0, len(daftar_kontak)) :
        kontak = daftar_kontak [i]
        if telepon == kontak["telepon"] :
            index = i
            break

    if index == -1 :
        print ("Data kontak tidak ditemukan")
    else :
        del daftar_kontak [index]
        print ("Berhasil menghapus data kontak")

# Cari Kontak 
def cari_kontak (daftar_kontak) :
    nama_dicari = input ("Nama yang dicari : ")

    for kontak in daftar_kontak :
        nama = kontak ["nama"]
        if nama.lower().find (nama_dicari.lower()) != -1 :
            print ("===========================")
            print (f"Nama : {kontak['nama']}")
            print (f"Email : {kontak['email']}")
            print (f"Telepon : {kontak['telepon']}")  


    