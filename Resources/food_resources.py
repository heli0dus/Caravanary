human_food_dictionary = {
    # days, description, size, cost
    "bread": (1, "", 1, 10),
    "crackers": (2, "", 2, 14),
    "cheese": (2, "", 1, 15),
    "jerky": (4, "", 2, 20),

}
animals_food_dictionary = {
    # days, description, size, cost
    "bran": (1, "", 1, 5),
    "fresh grass": (2, "", 1, 10),
    "hay": (3, "", 1, 17),
    "corn": (4, "", 2, 17),
}

human_food_variability = len(human_food_dictionary)
animals_food_variability = len(animals_food_dictionary)

# days - provides supplies for N days
# description - text description of good
# size - takes up N slots in inventory
# cost - cost N money by default

# TODO descriptions
# TODO more goods(?)
