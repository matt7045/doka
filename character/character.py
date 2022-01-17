#Base class definition for the character class. Every
# character has 
#   Attack
#   Defense
#   Magic
#   Speed
#   Health
class Character:
    def __init__(self,
                 attack,
                 defense,
                 magic,
                 speed,
                 health,
                 inventory_size = 0
                 ):
        self.attack         = attack
        self.defense        = defense
        self.magic          = magic
        self.speed          = speed
        self.health         = health
        self.inventory_size = inventory_size
        
        
        
