from random import randint
from random import random

class Character:
    def __init__(self):
        self.name = ""
        self.health = 1
        self.max_health = 1
        self.copper = 0
        self.silver = 0
        self.gold = 0
        self.potions = 0

    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print "%s's attack missed!" % self.name
        else: print random("%s hurts %s!" % (self.name, enemy.name),
                           "%s hits %s!" % (self.name, enemy.name),
                           "%s's attack hit %s!" % (self.name, enemy.name))
        return enemy.health <= 0
class Enemy(Character):
    def __init__(self, player):
        self.name = random("a goblin", "a dragon", " a big-ass-spider", "Jesus",
                           "David Bowie riding in on a cloud made of lightning")
class Player(Character):
    def __init__(self):
        Character.__init__(self)
