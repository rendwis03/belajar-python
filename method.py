# print merupakan method, dan teks diantara kutip merupakan parameter
print ("Belajar Method Parameter")


def say_hello (first_name, last_name) :
    print (f"Hello {first_name} {last_name}, Selamat Belajar dan Semangat yaa...")

say_hello ("Rendy", "Saputra")


# Default argument velue

def say_hello (first_name="Rendy", last_name="Saputra") :
    print (f"Hello {first_name} {last_name}, Selamat Belajar dan Semangat yaa...")

say_hello ()
say_hello ("Hafis", "Rabbani")
say_hello (last_name="Dwi")