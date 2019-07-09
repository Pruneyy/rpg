# A simple text based rpg

# Imports
import classes
import random

# Main
def main():
    m = classes.Healer()
    m.command(m.COMMANDS)
    print (m.attack(m.DICE))

# Running Main
if __name__ == '__main__':
    main()
