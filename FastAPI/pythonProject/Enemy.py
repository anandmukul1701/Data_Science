class Enemy:
    """
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def talk(self):
        print(f"I'm a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closure to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")
    """
    
        
    """
    type_of_enemy: str
    health_points: int
    attack_damage: int

    def __init__(self):
        pass

    def talk(self):
        print(f"I'm a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closure to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")
    """


    """
    # Constructors
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy ## This is public
        # self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I'm a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closure to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")    
    """    

    # Encapsulation
    def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I'm a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closure to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage.") 

    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def special_attack(self):
        print('Enemy has no special attack')