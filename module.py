print ("Belajar Module")

# Digunakan untuk memanggil function dari file lain

# Penulisan awalnya
# Pemanggilan harus diberikan .cth_module
'''
import cth_module 
hello = cth_module.hello("Rendy") 
print (hello)
'''

# Bisa jika ditulis seperti berikut
# Pemanggilan tidak perlu .cth_module
from cth_module import hello
hello = hello("Rendy") 

from cth_module import total
hasil = total
print (hasil)
