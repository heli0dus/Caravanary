from Resources import animal_food, animals, armory, hireable, human_food, luxury, weapons

tradeable_goods = {

}

# Reminder:
# [0]  - dicttype
# [-1] - cost
# [-2] - size
# [-3] - description

all_dictionaries = (
    animal_food.animals_food_dictionary,    # 1
    animals.animals_dictionary,             # 7
    armory.armor_dictionary,               # 3
    hireable.hireable_dictionary,           # 6
    human_food.human_food_dictionary,       # 0
    luxury.luxury_dictionary,               # 4
    weapons.weapon_dictionary,              # 2
)


def det_dict_type(dict_name):
    if dict_name == animal_food.animals_food_dictionary:
        return "animal_food"
    if dict_name == animals.animals_dictionary:
        return "animal"
    if dict_name == armory.armor_dictionary:
        return "armor"
    if dict_name == hireable.hireable_dictionary:
        return "hireable"
    if dict_name == human_food.human_food_dictionary:
        return "human_food"
    if dict_name == luxury.luxury_dictionary:
        return "luxury"
    if dict_name == weapons.weapon_dictionary:
        return "weapon"


def collect_all_goods():
    for i in all_dictionaries:
        for j in i.keys():
            if j != "none":
                obj_type = det_dict_type(i)
                stats_list = [obj_type]
                for k in i[j]:
                    stats_list.append(k)
                tradeable_goods[j] = stats_list
