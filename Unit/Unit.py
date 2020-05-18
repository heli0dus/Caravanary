import random as rnd
from Resources import weapons, armory, names


class Unit:
    def __init__(self, name, hp, low_dmg, high_dmg, armor, evade_chance, accuracy):
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__low_dmg = low_dmg
        self.__high_dmg = high_dmg
        self.__armor = armor
        self.__evade_chance = evade_chance
        self.__accuracy = accuracy

    # property = getter
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def max_hp(self):
        return self.__max_hp

    @property
    def name(self):
        return self.__name

    @property
    def low_dmg(self):
        return self.__low_dmg

    @property
    def high_dmg(self):
        return self.__high_dmg

    @property
    def armor(self):
        return self.__armor

    @property
    def evade_chance(self):
        return self.__evade_chance

    @property
    def accuracy(self):
        return self.__accuracy

    # log death event
    def die(self):
        print(self.name + " died")

    def is_alive(self):
        return self.hp > 0

    def hit(self, a):
        if isinstance(a, Unit):
            hit = rnd.randint(0, 100) + self.accuracy()
            if hit > a.evade_chance:
                dmg = rnd.randint(self.low_dmg, self.high_dmg) - a.armor
                if dmg > 0:
                    a.hp -= dmg
                    print(self.name + " dealt " + str(dmg) + " damage to " + a.name)
                    if a.hp < 0:
                        a.die()
                else:
                    print(self.name + " could't hit through " + a.name + "'s armor")
            else:
                print(self.name + " tried to hit " + a.name + " but it was a miss")
        else:
            raise AttributeError

    # not straight fabric constructor using game items
    @classmethod
    def unit_generator(cls, name=rnd.choice(names.names),
                       weapon=rnd.choice(tuple(weapons.weapon_dictionary)),
                       armor=rnd.choice(tuple(armory.armor_dictionary)),
                       strength=rnd.randint(1, 3),
                       dexterity=rnd.randint(1, 3)):

        if weapon in weapons.weapon_dictionary.keys() and \
                armor in armory.armor_dictionary.keys() and strength > 0 and dexterity > 0:

            weapon_vector = weapons.weapon_dictionary[weapon]
            armor_vector = armory.armor_dictionary[armor]

            obj_name = name
            obj_hp = 20 + 5 * strength
            obj_low_dmg = 1 + strength + weapon_vector[0]
            obj_high_dmg = 2 + strength * 2 + weapon_vector[1]
            obj_accuracy = dexterity * 5 + weapon_vector[2]
            obj_evade_chance = 40 + dexterity * 5 + armor_vector[1]
            obj_armor = armor_vector[0]

            return cls(obj_name, obj_hp, obj_low_dmg, obj_high_dmg,
                       obj_armor, obj_evade_chance, obj_accuracy)
        else:
            raise AttributeError
