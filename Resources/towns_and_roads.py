specialization_type = {
    # human_food(1), animal_food(2), weapon(3), armor(4), luxury(5), slaves(6), hireable(7), animals(8)
    "poor": (1, 1, 1, 1, 1, 1, 1, 1),
    "normal": (1, 1, 1, 1, 1, 1, 1, 1),
}

richness_type = {
    # human_food(1), animal_food(2), weapon(3), armor(4), luxury(5), slaves(6), hireable(7), animals (8)
    "poor": (1, 1, 1, 1, 1, 1, 1, 1),
    "normal": (1, 1, 1, 1, 1, 1, 1, 1),
}

point_type = (
    "Market",
    "Armory",
    "Mercenary Guild",
    "Bestiary",
    "Slave Market"
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
