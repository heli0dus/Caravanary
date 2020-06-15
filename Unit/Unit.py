import random as rnd
from Resources import weapons, armory, names


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
    def unit_generator(cls,
                       name=rnd.choice(names.names),
                       weapon=rnd.choice(tuple(weapons.weapon_dictionary)),
                       armor=rnd.choice(tuple(armory.armor_dictionary)),
                       strength=rnd.randint(1, 3),
                       dexterity=rnd.randint(1, 3),
                       ):

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

            return Unit(obj_name, obj_hp, obj_low_dmg, obj_high_dmg,
                       obj_armor, obj_evade_chance, obj_accuracy)
        else:
            raise AttributeError

    # fabric constructor using dictionaries of items
    @classmethod
    def random_unit_generator(cls,
                              weapon_dict=weapons.weapon_dictionary,
                              armor_dict=armory.armor_dictionary,
                              name_dict=names.names,

                              strength=rnd.randint(1, 3),
                              dexterity=rnd.randint(1, 3),
                              ):
        name = rnd.choice(name_dict)
        weapon = rnd.choice(tuple(weapon_dict))
        armor = rnd.choice(tuple(armor_dict))
        if weapon in weapon_dict.keys() and \
                armor in armor_dict.keys() and strength > 0 and dexterity > 0:

            weapon_vector = weapon_dict[weapon]
            armor_vector = armor_dict[armor]

            obj_name = name
            obj_hp = 20 + 5 * strength
            obj_low_dmg = 1 + strength + weapon_vector[0]
            obj_high_dmg = 2 + strength * 2 + weapon_vector[1]
            obj_accuracy = dexterity * 5 + weapon_vector[2]
            obj_evade_chance = 40 + dexterity * 5 + armor_vector[1]
            obj_armor = armor_vector[0]

            return Unit(obj_name, obj_hp, obj_low_dmg, obj_high_dmg, obj_armor, obj_evade_chance, obj_accuracy)
        else:
            raise AttributeError

    # bandits generators
    @classmethod
    def thief_generator(cls):
        return cls.random_unit_generator(weapons.thief, armory.thief, "thief")

    @classmethod
    def pickpocket_generator(cls):
        return cls.random_unit_generator(weapons.pickpocket, armory.pickpocket, "pickpocket")

    @classmethod
    def archer_generator(cls):
        return cls.random_unit_generator(weapons.archer, armory.archer, "archer")

    @classmethod
    def bouncer_generator(cls):
        return cls.random_unit_generator(weapons.bouncer, armory.bouncer, "bouncer")

    @classmethod
    def deserter_generator(cls):
        return cls.random_unit_generator(weapons.deserter, armory.deserter, "desrter")

    @classmethod
    def killer_generator(cls):
        return cls.random_unit_generator(weapons.killer, armory.killer, "killer")

    @classmethod
    def leader_generator(cls):
        return cls.random_unit_generator(weapons.leader, armory.leader, "bandit leader")


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
            self.evade_chance = self.armor - armory.armor_dictionary[self.clothes][1] + armory.armor_dictionary[armor][
                1]

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


class Mercenary(Unit):

    def __init__(self, unit, salary, type):
        super().__init__(unit.name, unit.hp, unit.low_dmg, unit.high_dmg, unit.armor, unit.evade_chance,
                                        unit.accuracy)
        self.salary = salary
        self.type = type

    @classmethod
    def rookie_generator(cls):
        return cls(super().random_unit_generator(weapons.rookie, armory.rookie), rnd.randint(5, 10), "Rookie")

    @classmethod
    def defender_generator(cls):
        return cls(super().random_unit_generator(weapons.defender, armory.defender), rnd.randint(5, 10), "Defender")

    @classmethod
    def soldier_generator(cls):
        return cls(super().random_unit_generator(weapons.soldier, armory.soldier), rnd.randint(5, 10), "Soldier")

    @classmethod
    def guardian_generator(cls):
        return cls(super().random_unit_generator(weapons.guardian, armory.guardian), rnd.randint(5, 10), "Guardian")

    @classmethod
    def assassin_generator(cls):
        return cls(super().random_unit_generator(weapons.assassin, armory.assassin), rnd.randint(5, 10), "Assassin")

    @classmethod
    def hero_generator(cls):
        return cls(super().random_unit_generator(weapons.hero, armory.hero), rnd.randint(5, 10), "Hero")

    @classmethod
    def ultimate_generator(cls):
        return cls(super().random_unit_generator(weapons.ultimate, armory.ultimate), rnd.randint(5, 10), "Ultimate")

    def print(self):
        print(self.type, self.name)
        self.print_attack_stats()
        self.print_living_stats()
        print("salary:", self.salary)
        print()
