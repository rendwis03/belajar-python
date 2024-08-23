class mahasiswa :
# Class Variable / Variabel Statik
    jumlah = 0

    def __init__ (identitas, nama, nim, jurusan) :
# Instance Vatiable
        identitas.name = nama
        identitas.kode = nim
        identitas.major = jurusan
        mahasiswa.jumlah += 1
        print (f'Identitas dari {nama} memiliki nim {nim} yang diartikan berada di jurusan {jurusan}')

mhs1 = mahasiswa ('Rendy', 111, 'Pendidikan')
print (mahasiswa.jumlah)
mhs2 = mahasiswa ('Dwi', 222, 'Administrasi')
print (mahasiswa.jumlah)
mhs3 = mahasiswa ('Saputra', 333, 'Perkantoran')
print (mahasiswa.jumlah)

print (mhs1.__dict__)
print (mhs2.__dict__)
print (mhs3.__dict__)
