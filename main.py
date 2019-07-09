# A simple text based rpg

# Imports
import classes
import random
import gen

# Main
def main():
    intro()
    g = gen.Generator()
    g.gen_level()
    g.gen_tiles_level()

def intro():
    print ('###############')
    print ('')
    print ('###############')

# Running Main
if __name__ == '__main__':
    main()
