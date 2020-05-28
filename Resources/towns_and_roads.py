specialization_type = {
    # human_food(0), animal_food(1), weapon(2), armor(3), luxury(4), slaves(5), hireable(6), animals(7)
    "farm": (1, 1, 1, 1, 1, 1, 1, 1),
    "forgery": (1, 1, 1, 1, 1, 1, 1, 1),
}

richness_type = {
    # human_food(0), animal_food(1), weapon(2), armor(3), luxury(4), slaves(5), hireable(6), animals (7)
    "poor": (1, 1, 1, 1, 1, 1, 1, 1),
    "normal": (1, 1, 1, 1, 1, 1, 1, 1),
}

point_type = (
    "Market",
    "Armory",
    "Mercenary Guild",
    "Bestiary",
    "Slave Market",
    "Luxury"
)

towns_names = (
    "One",
    "Two",
    "Three",
)

roadsMatrix = (
  # to1 to2 to3
    (0,  2,  3),  # One (1)
    (4,  0,  6),  # Two (2)
    (7,  8,  0),  # Three (3)
)
