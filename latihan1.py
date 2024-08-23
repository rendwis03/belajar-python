print ('latihan komparasi dan logika')

# Membuat Program sederhana +++++3-----10+++++
inputUser = int (input('-OR- \n Masukkan angka yang bernilai \n kurang dari 3 \n atau \n lebih besar dari 10 \n ==>'))

# +++++3----- > Memeriksa angka yang kurang dari 3
angkaKecil = (inputUser < 3)
print (f'kurang dari 3 => {angkaKecil}')

# -----10+++++ > Memeriksa angka yang lebih besar dari 10
angkaBesar = (inputUser > 10)
print (f'lebih dari 10 => {angkaBesar}')

# Pengidentifikasian
final = angkaKecil or angkaBesar
print (f'Angka yang anda masukkan {3*('=')} {final}')

print (f'\n {10*('=')} \n') # Pemisah pernyataan

# -----3+++++10----- > kasus irisan
inputUser = int (input(' -AND- \n Masukkan angka yang bernilai \n lebih dari 3 \n dan \n kecil dari 10 \n ==>'))

# -----3+++++
angkaKecil = (inputUser > 3)
print (f'lebih dari 3 => {angkaKecil}')

# +++++10-----
angkaBesar = (inputUser < 10)
print (f'kurang dari 10 => {angkaBesar}')

# Pengidentifikasian
final = angkaKecil and angkaBesar
print (f'Angka yang anda masukkan {3*('=')} {final}')
