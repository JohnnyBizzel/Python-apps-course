import random


class Creature:
    # magic method!
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    # def __init__(self, name, level):  # inherited from base class
    #     super().__init__(name,level)

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(self.name, creature.name))
        # roll 12 sided dice..
        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()
        print("{} rolls {}".format(self.name, my_roll))
        print("{} rolls {}".format(creature.name, creature_roll))
        print()

        if my_roll >= creature_roll:

            print("{} has **defeated** {}".format(self.name, creature.name))
            self.level += 1
            print("{} is now level {}".format(self.name, self.level))
            return True
        else:
            print("{} has been DEFEATED :(".format(self.name))
            return False


class SmallAnimal(Creature):
    # Override the base class method
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        # >>>>-- replace with ternary operator:
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier




