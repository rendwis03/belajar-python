print ("Belajar Continue dan break")

for i in range (0, 100) :
    if i % 2 == 1 :
        continue
    print (i)

# break digunakan me-stop perulangan
while True :
    data = input("Masukkan String ; ")
    if data == "p" :
        break
    print (data)