from Resources import towns_and_roads, food_resources
import random as random

class TradePoint:
    def __init__(self, town, point_type):
        self.town = town
        self.point_type = point_type
        self.specialization_multipliers = towns_and_roads.specialization_type[town.specialization]
        self.richness_multipliers = towns_and_roads.richness_type[town.richness]
        if town.size < 3:
            if point_type == "Market":
                for i in range(2):
                    randnum = random.randint(1, food_resources.human_food_variability+food_resources.animals_food_variability)
                    if randnum > food_resources.human_food_variability:
                        self.goods_map = {food_resources.animals_food_dictionary.keys()[randnum - food_resources.human_food_variability - 1],
                                          food_resources.animals_food_dictionary[food_resources.animals_food_dictionary.keys()[randnum - food_resources.human_food_variability - 1]]}
                    else:
                        self.goods_map = {food_resources.human_food_dictionary.keys()[randnum - 1],
                                          food_resources.human_food_dictionary[food_resources.human_food_dictionary.keys()[randnum - 1]]}
# TODO
