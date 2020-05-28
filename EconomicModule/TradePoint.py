from Resources import towns_and_roads, food_resources, armory, weapons, animals, luxury, hireable, slaves
import random as random


class TradePoint:
    def __init__(self, town, point_type):
        self.town = town
        self.point_type = point_type
        self.specialization_multipliers = towns_and_roads.specialization_type[town.specialization]
        self.richness_multipliers = towns_and_roads.richness_type[town.richness]
        self.goods_map = {}
        if town.size < 3:
            repeatings = 1
        elif (town.size < 6) and (town.size > 2):
            repeatings = 3
        elif (town.size > 5) and (town.size < 10):
            repeatings = 4
        else:
            repeatings = 5
        for j in range(repeatings):
            random_multiplier = 1 + (random.randint(1, 150) / 100)
            if point_type == "Market":
                for i in range(3):
                    randnum = random.randint(1, food_resources.human_food_variability + food_resources.animals_food_variability)
                    print("(", end="")  # Temporal
                    print(randnum, end="")  # Temporal
                    print(") ", end="")  # Temporal
                    # random_multiplier = 1 + (random.randint(1, 150)/100)
                    if randnum > food_resources.human_food_variability:
                        # for animal_food
                        self.goods_map[list(food_resources.animals_food_dictionary.keys())[randnum - food_resources.human_food_variability - 1]] = \
                            food_resources.animals_food_dictionary[list(food_resources.animals_food_dictionary.keys())[randnum - food_resources.human_food_variability - 1]][-1] * \
                            self.specialization_multipliers[1] * self.richness_multipliers[1] * random_multiplier // 0.01 / 100
                        print("Added: ", list(food_resources.animals_food_dictionary.keys())[
                            randnum - food_resources.human_food_variability - 1], '\n')  # Temporal
                    else:
                        # for human_food
                        self.goods_map[list(food_resources.human_food_dictionary.keys())[randnum - 1]] = \
                            food_resources.human_food_dictionary[list(food_resources.human_food_dictionary.keys())[randnum - 1]][-1] * \
                            self.specialization_multipliers[0] * self.richness_multipliers[0] * random_multiplier // 0.01 / 100
                        print("Added: ", list(food_resources.human_food_dictionary.keys())[randnum - 1], '\n')  # Temporal
            if point_type == "Armory":
                randnum = random.randint(1, armory.armor_variability + weapons.weapon_variability)
                print("(", end="")  # Temporal
                print(randnum, end="")  # Temporal
                print(") ", end="")  # Temporal
                # random_multiplier = 1 + (random.randint(1, 150) / 100)
                if randnum > armory.armor_variability:
                    # for weapon
                    self.goods_map[list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1]] = \
                        weapons.weapon_dictionary[list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1]][-1] * \
                        self.specialization_multipliers[2] * self.richness_multipliers[2] * random_multiplier // 0.01 / 100
                    print("Added: ", list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1], '\n')  # Temporal
                else:
                    # for armor
                    self.goods_map[list(armory.armor_dictionary.keys())[randnum - 1]] = \
                        armory.armor_dictionary[list(armory.armor_dictionary.keys())[randnum - 1]][-1] * \
                        self.specialization_multipliers[3] * self.richness_multipliers[3] * random_multiplier // 0.01 / 100
                    print("Added: ", list(armory.armor_dictionary.keys())[randnum - 1], '\n')  # Temporal
            if point_type == "Bestiary":
                randnum = random.randint(1, animals.animals_variability)
                print("(", end="")  # Temporal
                print(randnum, end="")  # Temporal
                print(") ", end="")  # Temporal
                # random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for animals
                self.goods_map[list(animals.animals_dictionary.keys())[randnum - 1]] = \
                    animals.animals_dictionary[list(animals.animals_dictionary.keys())[randnum - 1]][-1] * \
                    self.specialization_multipliers[7] * self.richness_multipliers[7] * random_multiplier // 0.01 / 100
                print("Added: ", list(animals.animals_dictionary.keys())[randnum - 1], '\n')  # Temporal
            if point_type == "Luxury":
                randnum = random.randint(1, luxury.luxury_variability)
                print("(", end="")  # Temporal
                print(randnum, end="")  # Temporal
                print(") ", end="")  # Temporal
                # random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for luxury
                self.goods_map[list(luxury.luxury_dictionary.keys())[randnum - 1]] = \
                    luxury.luxury_dictionary[list(luxury.luxury_dictionary.keys())[randnum - 1]][-1] * \
                    self.specialization_multipliers[4] * self.richness_multipliers[4] * random_multiplier // 0.01 / 100
                print("Added: ", list(luxury.luxury_dictionary.keys())[randnum - 1], '\n')  # Temporal
            if point_type == "Mercenary Guild":
                randnum = random.randint(1, hireable.hireable_variability)
                print("(", end="")  # Temporal
                print(randnum, end="")  # Temporal
                print(") ", end="")  # Temporal
                # random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for hireable
                self.goods_map[list(hireable.hireable_dictionary.keys())[randnum - 1]] = \
                    hireable.hireable_dictionary[list(hireable.hireable_dictionary.keys())[randnum - 1]][-1] * \
                    self.specialization_multipliers[6] * self.richness_multipliers[6] * random_multiplier // 0.01 / 100
                print("Added: ", list(hireable.hireable_dictionary.keys())[randnum - 1], '\n')  # Temporal
            if point_type == "Slave Market":
                randnum = random.randint(1, slaves.slaves_variability)
                print("(", end="")  # Temporal
                print(randnum, end="")  # Temporal
                print(") ", end="")  # Temporal
                # random_multiplier = 1 + (random.randint(1, 150) / 100)
                # for slaves
                self.goods_map[list(slaves.slaves_dictionary.keys())[randnum - 1]] = \
                    slaves.slaves_dictionary[list(slaves.slaves_dictionary.keys())[randnum - 1]][-1] * \
                    self.specialization_multipliers[5] * self.richness_multipliers[5] * random_multiplier // 0.01 / 100
                print("Added: ", list(slaves.slaves_dictionary.keys())[randnum - 1], '\n')  # Temporal

    def ret_goods_map(self):
        s = ""
        for i in self.goods_map.keys():
            s = (s + i + ", cost: " + self.goods_map[i].__str__() + "\n")
        return s[:-1]

    def __str__(self):
        return self.point_type + ":" + '\n' + self.ret_goods_map()


# TODO      goods descriptions
# TODO      goods size
# TODO      delete all #Temporal
# TODO      refactor imports
