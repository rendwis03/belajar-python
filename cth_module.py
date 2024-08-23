print ("Sumber dari Belajar Module")

def hello (nama) :
    return f"Hello {nama}"

def total (*list_angka) :
    hasil = 0
    for data in list_angka :
        hasil = hasil + data
    return (list_angka, hasil)
list_angka, hasil = total (12, 32, 42)
total = f"Penjumlahan dari {list_angka} ialah {hasil}"


