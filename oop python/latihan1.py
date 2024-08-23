print ('Game Sederhana by "Kelas Terbuka"')

class Hero :
    def __init__(self, name, health, attackPower, armorNumber) :
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang (self, lawan) :
        print (f'{self.name} sedang menyerang {lawan.name}')
        lawan.diserang (self, self.attackPower) 

    def diserang (self, lawan, attackPower_lawan) :
        print (f'{self.name} sedang diserang {lawan.name}')
        attackDiterima = attackPower_lawan / self.armorNumber 
        print (f'serangan terasa : {str(attackDiterima)}')
        self.health -= attackDiterima
        print (f'darah {self.name} tersisa {str(self.health)}')
    

sniper = Hero ('sniper', 100, 10, 5)
rikimaru = Hero ('rikimaru', 100, 20, 10)

sniper.serang (rikimaru)
print (f'|{40*('=')}|')
rikimaru.serang (sniper)

    