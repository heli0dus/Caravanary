from Resources import towns_and_roads, human_food, armory, weapons, animals, luxury, hireable, slaves
from Resources import animal_food, animals, armory, hireable, human_food, luxury, weapons
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
            random_multiplier = 1 + (random.randint(50, 300) / 100)
            if point_type == "Market":
                for i in range(3):
                    for k in range(2):
                        if k == 0:
                            randnum = random.randint(1, human_food.human_food_variability)
                            # print("(", end="")  # Temporal
                            # print(randnum, end="")  # Temporal
                            # print(") ", end="")  # Temporal
                            # for human_food
                            self.goods_map[list(human_food.human_food_dictionary.keys())[randnum - 1]] = int(\
                            human_food.human_food_dictionary[list(human_food.human_food_dictionary.keys())[randnum - 1]][-1] * \
                            self.specialization_multipliers[0] * self.richness_multipliers[0] * random_multiplier // 1)
                            # print("Added: ", list(human_food.human_food_dictionary.keys())[randnum - 1])  # Temporal
                        if k == 1:
                            randnum = random.randint(1, animal_food.animals_food_variability)
                            # print("(", end="")  # Temporal
                            # print(randnum, end="")  # Temporal
                            # print(") ", end="")  # Temporal
                            # for animal_food
                            self.goods_map[list(animal_food.animals_food_dictionary.keys())[randnum-1]] = int(\
                            animal_food.animals_food_dictionary[list(animal_food.animals_food_dictionary.keys())[randnum-1]][-1] * \
                            self.specialization_multipliers[1] * self.richness_multipliers[1] * random_multiplier // 1)
                            # print("Added: ", list(animal_food.animals_food_dictionary.keys())[randnum-1])  # Temporal

            #         randnum = random.randint(1, human_food.human_food_variability + human_food.animals_food_variability)
            #         print("(", end="")  # Temporal
            #         print(randnum, end="")  # Temporal
            #         print(") ", end="")  # Temporal
            #         if randnum > human_food.human_food_variability:
            #             # for animal_food
            #             self.goods_map[list(human_food.animals_food_dictionary.keys())[randnum - human_food.human_food_variability - 1]] = \
            #                 human_food.animals_food_dictionary[list(human_food.animals_food_dictionary.keys())[randnum - human_food.human_food_variability - 1]][-1] * \
            #                 self.specialization_multipliers[1] * self.richness_multipliers[1] * random_multiplier // 1
            #             print("Added: ", list(human_food.animals_food_dictionary.keys())[
            #                 randnum - human_food.human_food_variability - 1])  # Temporal
            #         else:
            #             # for human_food
            #             self.goods_map[list(human_food.human_food_dictionary.keys())[randnum - 1]] = \
            #                 human_food.human_food_dictionary[list(human_food.human_food_dictionary.keys())[randnum - 1]][-1] * \
            #                 self.specialization_multipliers[0] * self.richness_multipliers[0] * random_multiplier // 1
            #             print("Added: ", list(human_food.human_food_dictionary.keys())[randnum - 1])  # Temporal
            # randnum = random.randint(1, armory.armor_variability + weapons.weapon_variability)
            #     print("(", end="")  # Temporal
            #     print(randnum, end="")  # Temporal
            #     print(") ", end="")  # Temporal
            #     if randnum > armory.armor_variability:
            #         # for weapon
            #         self.goods_map[list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1]] = \
            #             weapons.weapon_dictionary[list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1]][-1] * \
            #             self.specialization_multipliers[2] * self.richness_multipliers[2] * random_multiplier // 1
            #         print("Added: ", list(weapons.weapon_dictionary.keys())[randnum - armory.armor_variability - 1])  # Temporal
            #     else:
            #         # for armor
            #         self.goods_map[list(armory.armor_dictionary.keys())[randnum - 1]] = \
            #             armory.armor_dictionary[list(armory.armor_dictionary.keys())[randnum - 1]][-1] * \
            #             self.specialization_multipliers[3] * self.richness_multipliers[3] * random_multiplier // 1
            #         print("Added: ", list(armory.armor_dictionary.keys())[randnum - 1])  # Temporal

            if point_type == "Armory":
                for k in range(2):
                    if k == 0:
                        randnum = random.randint(1, weapons.weapon_variability-1)
                        # print("(", end="")  # Temporal
                        # print(randnum, end="")  # Temporal
                        # print(") ", end="")  # Temporal
                        # for weapon
                        self.goods_map[list(weapons.weapon_dictionary.keys())[randnum - 1]] = int(\
                        weapons.weapon_dictionary[list(weapons.weapon_dictionary.keys())[randnum - 1]][-1] * \
                        self.specialization_multipliers[2] * self.richness_multipliers[2] * random_multiplier // 1)
                        # print("Added: ", list(weapons.weapon_dictionary.keys())[randnum - 1])  # Temporal
                    if k == 1:
                        randnum = random.randint(1, armory.armor_variability-1)
                        # print("(", end="")  # Temporal
                        # print(randnum, end="")  # Temporal
                        # print(") ", end="")  # Temporal
                        # for armor
                        self.goods_map[list(armory.armor_dictionary.keys())[randnum - 1]] = int(\
                        armory.armor_dictionary[list(armory.armor_dictionary.keys())[randnum - 1]][-1] * \
                        self.specialization_multipliers[3] * self.richness_multipliers[3] * random_multiplier // 1)
                        # print("Added: ", list(armory.armor_dictionary.keys())[randnum - 1])  # Temporal

            if point_type == "Bestiary":
                randnum = random.randint(1, animals.animals_variability)
                # print("(", end="")  # Temporal
                # print(randnum, end="")  # Temporal
                # print(") ", end="")  # Temporal
                # for animals
                self.goods_map[list(animals.animals_dictionary.keys())[randnum - 1]] = int(\
                animals.animals_dictionary[list(animals.animals_dictionary.keys())[randnum - 1]][-1] * \
                self.specialization_multipliers[7] * self.richness_multipliers[7] * random_multiplier // 1)
                # print("Added: ", list(animals.animals_dictionary.keys())[randnum - 1])  # Temporal

            if point_type == "Luxury":
                randnum = random.randint(1, luxury.luxury_variability)
                # print("(", end="")  # Temporal
                # print(randnum, end="")  # Temporal
                # print(") ", end="")  # Temporal
                # for luxury
                self.goods_map[list(luxury.luxury_dictionary.keys())[randnum - 1]] = int(\
                luxury.luxury_dictionary[list(luxury.luxury_dictionary.keys())[randnum - 1]][-1] * \
                self.specialization_multipliers[4] * self.richness_multipliers[4] * random_multiplier // 1)
                # print("Added: ", list(luxury.luxury_dictionary.keys())[randnum - 1])  # Temporal
            if point_type == "Mercenary Guild":
                merc_name = random.choice(list(hireable.hireable_dictionary.keys()))
                merc_obj = hireable.hireable_dictionary[merc_name][0]()
                self.goods_map[str(len(self.goods_map)+1)] = (merc_obj, int(hireable.hireable_dictionary[merc_name][-1] * \
                self.specialization_multipliers[6] * self.richness_multipliers[6] * random_multiplier // 1))
                # randnum = random.randint(1, hireable.hireable_variability)
                # # for hireable
                # self.goods_map[list(hireable.hireable_dictionary.keys())[randnum - 1]] = int(\
                # hireable.hireable_dictionary[list(hireable.hireable_dictionary.keys())[randnum - 1]][-1] * \
                # self.specialization_multipliers[6] * self.richness_multipliers[6] * random_multiplier // 1)
                # print("Added: ", list(hireable.hireable_dictionary.keys())[randnum - 1])  # Temporal

    # if point_type == "Slave Market":
    #     randnum = random.randint(1, slaves.slaves_variability)
    #     print("(", end="")  # Temporal
    #     print(randnum, end="")  # Temporal
    #     print(") ", end="")  # Temporal
    #
    #     # for slaves
    #     self.goods_map[list(slaves.slaves_dictionary.keys())[randnum - 1]] = \
    #         slaves.slaves_dictionary[list(slaves.slaves_dictionary.keys())[randnum - 1]][-1] * \
    #         self.specialization_multipliers[5] * self.richness_multipliers[5] * random_multiplier // 1
    #     print("Added: ", list(slaves.slaves_dictionary.keys())[randnum - 1])  # Temporal

    def ret_goods_map(self):
        if self.point_type == "Mercenary Guild":
            s = ""
            for i in self.goods_map.keys():
                s = (s + i + ") " + self.goods_map[i][0].name + " (" + self.goods_map[i][0].type + "), salary: " +
                str(self.goods_map[i][0].salary) + ", cost: " + str(self.goods_map[i][1]) + "\n")
            return s[:-1]
        else:
            s = ""
            for i in self.goods_map.keys():
                s = (s + i + ", cost: " + self.goods_map[i].__str__() + "\n")
            return s[:-1]

    def __str__(self):
        return self.point_type + ":" + '\n' + self.ret_goods_map()
