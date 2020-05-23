from Resources import towns_and_roads, food_resources, armory, weapons, animals, luxury, hireable, slaves
import random as random


print(slaves.slaves_variability)

class TradePoint:
    def __init__(self, town, point_type):
        self.town = town
        self.point_type = point_type
        self.specialization_multipliers = towns_and_roads.specialization_type[town.specialization]
        self.richness_multipliers = towns_and_roads.richness_type[town.richness]
# TODO      another town sizes
        if town.size < 3:
            repeatings = 1
        if (town.size < 6)and(town.size>2):
            repeatings = 3
        for j in range(repeatings):
            if point_type == "Market":
                for i in range(3):
                    randnum = random.randint(1, food_resources.human_food_variability+food_resources.animals_food_variability)
                    random_multiplier = 1 + (random.randint(1, 150)/100)
                    if randnum > food_resources.human_food_variability:
                        # for animal_food
                        self.goods_map = {food_resources.animals_food_dictionary.keys()[randnum - food_resources.human_food_variability - 1],
                                          food_resources.animals_food_dictionary[food_resources.animals_food_dictionary.keys()[randnum - food_resources.human_food_variability - 1]][-1]
                                          * self.specialization_multipliers[2] * self.richness_multipliers[2] * random_multiplier}
                    else:
                        # for human_food
                        self.goods_map = {food_resources.human_food_dictionary.keys()[randnum - 1],
                                          food_resources.human_food_dictionary[food_resources.human_food_dictionary.keys()[randnum - 1]][-1]
                                          * self.specialization_multipliers[1] * self.richness_multipliers[1] * random_multiplier}
            if point_type == "Armory":
                randnum = random.randint(1, armory.armor_variability+weapons.weapon_variability)
                random_multiplier = 1 + (random.randint(1, 150) / 100)
                if randnum > armory.armor_variability:
                    # for weapon
                    self.goods_map = {weapons.weapon_dictionary.keys()[randnum - armory.armor_variability - 1],
                                      weapons.weapon_dictionary[weapons.weapon_dictionary.keys()[randnum - armory.armor_variability - 1]][-1]
                                      * self.specialization_multipliers[3] * self.richness_multipliers[3] * random_multiplier}
                else:
                    # for armor
                    self.goods_map = {armory.armor_dictionary.keys()[randnum - 1],
                                      armory.armor_dictionary[armory.armor_dictionary.keys()[randnum - 1]][-1]
                                      * self.specialization_multipliers[4] * self.richness_multipliers[4] * random_multiplier}
            if point_type == "Bestiary":
                randnum = random.randint(1, animals.animals_variability)
                random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for animals
                self.goods_map = {animals.animals_dictionary.keys()[randnum - 1],
                                  animals.animals_dictionary[animals.animals_dictionary.keys()[randnum - 1]][-1]
                                  * self.specialization_multipliers[8] * self.richness_multipliers[8] * random_multiplier}
            if point_type == "Luxury Trade":
                randnum = random.randint(1, luxury.luxury_variability)
                random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for luxury
                self.goods_map = {luxury.luxury_dictionary.keys()[randnum - 1],
                                  luxury.luxury_dictionary[luxury.luxury_dictionary.keys()[randnum - 1]][-1]
                                  * self.specialization_multipliers[5] * self.richness_multipliers[5] * random_multiplier}
            if point_type == "Labor Exchange":
                randnum = random.randint(1, hireable.hireable_variability)
                random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for hireable
                self.goods_map = {hireable.hireable_dictionary.keys()[randnum - 1],
                                  hireable.hireable_dictionary[hireable.hireable_dictionary.keys()[randnum - 1]][-1]
                                  * self.specialization_multipliers[7] * self.richness_multipliers[7] * random_multiplier}
            if point_type == "Slave Market":
                randnum = random.randint(1, slaves.slaves_variability)
                random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for slaves
                self.goods_map = {slaves.slaves_dictionary.keys()[randnum - 1],
                                  slaves.slaves_dictionary[slaves.slaves_dictionary.keys()[randnum - 1]][-1]
                                  * self.specialization_multipliers[6] * self.richness_multipliers[6] * random_multiplier}
# TODO      trade function
# TODO      goods descriptions