import random as rnd
from Resouces import weapons, armory, names


class Unit:
    def __init__(self, name, hp, low_dmg, high_dmg, armor, evade_chance, accuracy):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.low_dmg = low_dmg
        self.high_dmg = high_dmg
        self.armor = armor
        self.evade_chance = evade_chance
        self.accuracy = accuracy

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

    def print_attack_stats(self):
        print("damage:", self.low_dmg, "-", self.high_dmg, "accuracy:", self.accuracy)

    def print_living_stats(self):
        print("health {0}/{1}, armor: {2}, evade: {3}".format(self.hp, self.max_hp, self.armor, self.evade_chance))

    def print(self):
        print(self.name)
        self.print_attack_stats()
        self.print_living_stats()
        print()

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


class Player(Unit):
    strength = 1
    dexterity = 1
    charisma = 1
    weapon = "none"
    clothes = "none"

    def __init__(self):
        super(Player, self).__init__("You", 25, 2, 4, 0, 45, 5)

    def set_weapon(self, weapon):
        if weapon in weapons.weapon_dictionary.keys():
            self.low_dmg -= weapons.weapon_dictionary[self.weapon][0]
            self.low_dmg -= weapons.weapon_dictionary[self.weapon][1]
            self.accuracy -= weapons.weapon_dictionary[self.weapon][2]

            self.low_dmg += weapons.weapon_dictionary[weapon][0]
            self.high_dmg += weapons.weapon_dictionary[weapon][1]
            self.accuracy += weapons.weapon_dictionary[weapon][2]

            self.weapon = weapon

    def set_clothes(self, armor):
        if armor in armory.armor_dictionary.keys():
            self.armor = self.armor - armory.armor_dictionary[self.clothes][0] + armory.armor_dictionary[armor][0]
            self.evade_chance = self.armor - armory.armor_dictionary[self.clothes][1] + armory.armor_dictionary[armor][1]

            self.clothes = armor

    def inc_str(self, num=1):
        self.strength += num
        self.max_hp += 5 * num
        self.low_dmg += num
        self.high_dmg += 2 * num

    def inc_dex(self, num=1):
        self.accuracy += 5 * num
        self.evade_chance += 5 * num
        self.dexterity += num

    def inc_char(self, num=1):
        self.charisma += num
