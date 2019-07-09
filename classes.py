import random
stat_description = ['HP ', 'Atk', 'Def', 'Agi']
equipment = ['Weapon', 'Shield', 'Armour']
w_increment = [3, 1, 2, 0]
a_increment = [1, 2, 0, 3]

# Hero class
class Hero:

    # Hero has a name, job, base stats, base level, base xp and amount of xp to level up
    def __init__(self, name, job, stats, level, xp, up=10):
        self.name = name
        self.job = job
        self.stats = stats
        self.level = level
        self.xp = xp
        self.up = up

    # Print your stats
    def print_details(self):

        # Prints the name, level and xp
        print('\n{} ({})\nLvl: {:>8}\nExp: {:>8}\n'.format(self.name, self.job, self.level, self.xp))
        
        # Prints stats (hp, atk, def, agi)
        for i, item in enumerate(self.stats):
            print('{}: {:>8}'.format(stat_description[i], item))
        print('\n')

    # Update xp after getting a kill
    def update_exp(self, xp):
        print ('Congratulations you gained {} xp'.format(xp))
        if (self.xp + xp) >= self.up:
            self.up = self.up + 0.5*self.up
            self.level = self.level + 1
            self.update_stats()
            print('Level = {} \nNext level = {} xp away'.format(self.level, int(self.up)))
            self.xp = 0
        else:
            self.xp = self.xp + xp
    
    # Update stats after levelling up
    def update_stats(self):
        if self.job == 'Warrior':
            for i in range(len(stat_description)):
                self.stats[i] = self.stats[i] + w_increment[i]
        elif self.job == 'Assassin':
            for i in range(len(stat_description)):
                self.stats[i] = self.stats[i] + a_increment[i]
            

class Monster():
    def __init__(self, name, level, stats):
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
        self.name = m[0]
        self.level = mon_level
        self.stats = mon_stat

    def print_monster(self):
        # Prints the name, level and xp
        print('\n{} \nLvl: {:>8}\n'.format(self.name, self.level))

        # Prints stats (hp, atk, def, agi)
        for i, item in enumerate(self.stats):
            print('{}: {:>8}'.format(stat_description[i], item))
        print('\n')


class Equipment():
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
    
    def print_equipment_header(self):
        print('{} {:>8} {:>8} {:>8} {:>8}'.format('Name      ', 'HP', 'Atk', 'Def', 'Agi'))
    
    def print_equipment(self):
        print('{}'.format(self.name), end='')
        for _ in range((10-len(self.name))):
            print(' ', end='')

        for item in self.stats:
            print (' {:>8}'.format(item), end='')
        print('\n')
