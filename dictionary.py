print ("Belajar Tipe Data Dictionary")

# key : velue

customer = {"name" : "Rendy", "age" : "21", "address" : "Surabaya"}

Name = customer["name"]
Age = customer["age"]
Address = customer["address"]

# Operasi dalam dictionary sama dengan list
# tambah dan mengubah data
customer["company"] = "PT Ala-Ala"
customer["name"] = "Hafis"
# menghapus data
del customer ["address"]

for key in customer :
    velue = customer [key]
    print (f"{key} : {velue}")

# Cara lain / yang mudah
print ("Cara Lain")
for key in customer.items() :
    print (f"{key[0]} : {key[1]}")

# Dalam bentuk ekstrak
print ("Bentuk Ekstrak dari Tipe Data Tuple")
for key, velue in customer.items():
    print (f"{key} : {velue}")

