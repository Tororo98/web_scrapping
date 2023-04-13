class soldier:
    # constructor de la clase
    def __init__(self, rank) -> None:
        self.rank = rank
        self.health = rank*1000
        self.strength = rank*100
        self.speed = rank*0.7
        self.flyes = False
    
    def take_wings(self):
        self.flyes = True

    def take_damage(self, dmg):
        self.health -= dmg

    def hit(self) -> int:
        return self.strength

tropa1 = soldier(3)
tropa1.take_wings()
tropa1.take_damage(200)
print(tropa1.health)