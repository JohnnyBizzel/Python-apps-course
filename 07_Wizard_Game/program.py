import time
import random
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()


def print_header():
    print('-------------------------------')
    print('      WIZARD BATTLE GAME')
    print('-------------------------------')
    print()
    game_loop()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 20, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you attack(a), run away(r), or look around(l) ?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard escapes and takes time to recover from his injuries...")
                time.sleep(5)  # rest for 5 seconds
                print("The wizard returns revitalized")
        elif cmd == 'r':
            print('{} is unsure of his power and flees!'.format(hero.name))
        elif cmd == 'l':
            print("{} peruses his surroundings and senses:".format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting')
            break

        if not creatures:
            print('You defeated all the creatures!')


if __name__ == '__main__':
    main()
