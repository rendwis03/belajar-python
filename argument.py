print ("Belajar Argument List")

def jumlahkan (*list_angka) :
    total = 0
    for angka in list_angka :
        total = total + angka
    print (f"Total dari {list_angka} berikut ialah : {total} ") 

jumlahkan (12, 23, 43, 32)

# return velue

def jumlahkan (*list_angka) :
    total = 0
    for angka in list_angka :
        total = total + angka
    return total

total = jumlahkan (12, 23, 43, 32)
print (total)


# Cara mengekstrak data

def jumlahkan (*list_angka) :
    total = 0
    for angka in list_angka :
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan (12, 23, 43, 32)
print (f"Hasil penjumlahan berikut {list_angka} ialah {total}")
