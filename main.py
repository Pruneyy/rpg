import classes
import random

def main():

    inventory = []
    inventory.append(classes.Equipment('Mace', [0, 3, 1, -1]))
    stat = [50, 50, 50, 50]
    name = input ('\nEnter a name for your hero: ').capitalize()
    c = input ('\nPick a class --> [W]arrior or [A]ssassin: ').lower()
    if c == 'w':
        hero = classes.Hero(name, 'Warrior', stat, 1, 0)
    elif c == 'a':
        hero = classes.Hero(name, 'Assassin', stat, 1, 0)
    else:
        print ('You did not pick a class, you have been assigned Warrior')
        hero = classes.Hero(name, 'Warrior', stat, 1, 0)

    hero.print_details()

    while True:

        what_do = input('Do you wish to [L]ook around, view [S]tats, view [I]nventory? ').lower()

        if what_do == 'l':
            mon = monster_maker()

            print ('\nYou come across a {}\n'.format(mon.name))
            mon.print_monster()
            cmd = input('\nDo you wish to [A]ttack or [R]un? ').lower()
            if cmd == 'a':
                print ('\nYou attack!\n')
                if attack_process(hero, mon):
                    hero.update_exp(xp_calc(mon.level))
                else:
                    break
            elif cmd == 'r':
                print ('\nYou escape!\n')
            else:
                print ('Exiting......')
                break


        elif what_do == 's':
            hero.print_details()
        elif what_do == 'i':
            inventory[0].print_equipment_header()
            for item in inventory:
                item.print_equipment()
        else:
            print ('Exiting....')
            break



def monster_maker():
    monsters = [
        ('Slime', 0), 
        ('Lizard', 1), 
        ('Snake', 2), 
        ('Boar', 3), 
        ('Brigand', 4), 
        ('Bear', 5), 
        ('Mammoth', 6), 
        ('Robot', 7),
        ('Guardian', 8), 
        ('Dragon', 9)
    ]

    m = random.choice(monsters)
    mon_stat = []
    for y in range(4):
        r_max = (m[1] * 10) + 9
        mon_stat.append(random.randint(m[1]*10, r_max))
        if y == 2:
            mon_level = random.randint(m[1]*10, r_max)
            if mon_level == 0:
                mon_level = 1
    mon = classes.Monster(m[0], mon_level, mon_stat)
    return mon

def attack_process(hero, monster):

    max_h_dmg = int(hero.stats[1] * 5 - monster.stats[2] * 2.5)
    max_m_dmg = int(monster.stats[1] * 5 - hero.stats[1] * 2.5)

    hero_health = hero.stats[0]*10
    mon_health = monster.stats[0]*10

    while hero_health > 0 or mon_health > 0:
        hero_damage = random.randint(1, max(1, max_h_dmg))
        mon_damage = random.randint(1, max(1, max_m_dmg))
        if mon_health - hero_damage > 0:
            mon_health = mon_health - hero_damage
            print ('{} deals {} damage --> {} has {} health remaining'.format(hero.name, int(hero_damage), monster.name, int(mon_health)))
            
            if hero_health - mon_damage > 0:
                hero_health = hero_health - mon_damage
                print ('{} deals {} damage --> {} has {} health remaining'.format(monster.name, int(mon_damage), hero.name, int(hero_health)))
            else:
                print ('{} deals {} damage --> {} has 0 health remaining'.format(monster.name, int(mon_damage), hero.name))
                print('\nYou have died\n')
                return False
        else:
            print ('{} deals {} damage --> {} has 0 health remaining'.format(hero.name, int(hero_damage), monster.name))
            print ('\nYou have defeated {}\n'.format(monster.name))
            return True
        
def xp_calc(level):
    xp = 10
    for i in range(level):
        if i < 2:
            continue
        else:
            xp = xp*1.1
            xp = int(xp)
    return xp

if __name__ == '__main__':
    main()