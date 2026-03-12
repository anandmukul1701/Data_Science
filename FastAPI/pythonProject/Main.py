from Enemy import *
from Zombie import *
from Ogre import *

"""
enemy1 = Enemy()
enemy1.type_of_enemy = 'Zombie'
# enemy2 = Enemy()
# enemy2.health_points = 9
# print(enemy2.health_points)
enemy1.talk()
enemy1.walk_forward()
enemy1.attack()
"""

"""
zombie = Enemy('Zombie', 1, 10)
zombie.talk()
zombie.walk_forward()
zombie.attack()
"""

"""
zombie = Enemy('Zombie', 10, 1)

# zombie.__type_of_enemy = "Ogre"
# print(zombie.__type_of_enemy)

# zombie.talk()
print(zombie.get_type_of_enemy())
"""
"""
zombie = Zombie('Zombie', 10, 1)
print(zombie.get_type_of_enemy())
"""

"""
zombie = Zombie(10, 1)
print(zombie.get_type_of_enemy())
zombie.talk()
zombie.spread_disease()
"""

"""
ogre = Ogre(10, 1)
print(ogre.get_type_of_enemy())
ogre.talk()
ogre.spread_disease()
"""

def battle(e: Enemy):
    e.talk()
    e.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)
battle(ogre)
