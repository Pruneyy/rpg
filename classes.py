# Classes for simple rpg

# Imports
import random

# Dice rolling function
def die(sides):
    return random.randint(1, sides)

# Character super class
class Character:
    
    # All characters have a name, hit chance, dodge change, inventory and exp
    def __init__ (self, name, hp, hit, dodge, inv, exp):
        self.name = name
        self.hp = hp
        self.hit = hit
        self.dodge = dodge
        self.inv = inv
        self.exp = exp

    # Print functionality
    def print_character(self):
        print ('{} {:>8} {:>8} {:>8} {:>8}'.format(self.name, self.hp, self.hit, self.dodge, self.exp))

    # All characters can fight
    def attack(self, roll):
        return die(roll)

# Player class - a subset of Character
class Player(Character):

    # Players need a name
    def __init__ (self, hp, exp):
        super().__init__(input("What is your name? ").capitalize(), hp, 20, 10, {}, exp)

    # Get command
    def command (self, commands):
        print ('Select an action:')
        for item in commands:
            print (item)
        return input('')

# Player class 1 --> Warrior
class Warrior(Player):

    # Constants for Warrior class
    LEVEL = 1
    LEVEL_2 = 10
    MAX_HP = 10
    DICE = 8
    COMMANDS = ['[A]ttack']
    PROF = 'Warrior'

    # Initialise the Warrior
    def __init__ (self):
        super().__init__(10, 0)

# Player class 2 --> Healer
class Healer(Player):

    # Constants for Healer class
    LEVEL = 1
    LEVEL_2 = 10
    MAX_HP = 10
    DICE = 6
    MANA = 3
    MAX_MANA = 3
    COMMANDS = ['[A]ttack', '[H]eal', '[M]ana Restore']
    PROF = 'Healer'

    # Initialise the Healer
    def __init__ (self):
        super().__init__(8, 0)

    # Heal ability
    def heal(self):
        return die(self.DICE)

    # Restore mana ability
    def mana_restore(self):
        return die(min(self.MAX_MANA, self.DICE))

# Player class 3 --> Mage
class Mage(Player):

    # Constants for Mage class
    LEVEL = 1
    LEVEL_2 = 10
    MAX_HP = 10
    DICE = 4
    MANA = 3
    MAX_MANA = 3
    COMMANDS = ['[A]ttack', '[M]agic Missile', '[F]ireball', '[G]enerate Mana']
    PROF = 'Mage'

    # Initialise the Mage
    def __init__ (self):
        super().__init__(6, 0)

    # Magic missile ability
    def missile(self, mana):

        damage = 0

        # Deals a random amount of damage as many times as how much mana is used
        for _ in range(mana):
            damage = damage + die(self.DICE)
        
        return damage

    # Fireball ability
    def fireball(self, mana):

        # Deals amount of mana used * single random dice roll
        return mana * die(self.DICE)

    # Regen mana ability
    def generate_mana(self):
        return die(min(self.MAX_MANA, self.DICE))

# Monster class - a subset of Character
class Monster(Character):
    
    # Initialising Monsters
    def __init__ (self, name, hp, exp=0):
        super().__init__(name, hp, 20, 10, {}, exp)

# Monster Class 1 --> Goblin
class Goblin(Monster):
    
    # Constants for Goblin class
    MAX_HP = 10
    DICE = 4

    # Initialise the Goblin
    def __init__ (self):
        super().__init__('Goblin',10, 0)

# Monster Class 2 --> Orc
class Orc(Monster):
    
    # Constants for Orc class
    MAX_HP = 20
    DICE = 6

    # Initialise the Orc
    def __init__ (self):
        super().__init__('Orc',20, 0)

# Monster Class 3 --> Ogre
class Ogre(Monster):
    
    # Constants for Ogre class
    MAX_HP = 30
    DICE = 8

    # Initialise the Ogre
    def __init__ (self):
        super().__init__('Ogre',30, 0)
