print ("Belajar List")

nama = ["Rendy", "Doni", "Adit"]
nama.append ("Roni")    # Untuk menambahkan data

print (nama)

# memanggil sesuai index atau mengakses
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])

# untuk mengetahui jumlah data, menggunakan -len()-
print (len(nama))

nama.remove ("Roni") # Untuk menghapus data
print (nama)

print (nama[0])
print (nama[1])
print (nama[2])

# mengubah data
nama [0] = "Hito"
print (nama)

