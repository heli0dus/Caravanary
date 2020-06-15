import EconomicModule.Town as Town

specialization_type = {
    # human_food(0), animal_food(1), weapon(2), armor(3), luxury(4), slaves(5), hireable(6), animals(7)
    "farm": (0.8, 0.8, 1.2, 1.4, 2, 0, 1.7, 0.9),
    "forgery": (1, 1.2, 0.9, 0.8, 1.5, 0, 1.4, 1.2),
    "Capital": (1.5, 1.3, 1.2, 1.2, 1.2, 0, 1, 1.4),
    "Port": (1, 1, 1.2, 1, 1.3, 0, 1.2, 1.3),
}

richness_type = {
    # human_food(0), animal_food(1), weapon(2), armor(3), luxury(4), slaves(5), hireable(6), animals(7)
    "poor": (1, 1, 1, 1, 1, 1, 1, 1),
    "normal": (1, 1, 1, 1, 1, 1, 1, 1),
}

point_type = (
    "Market",
    "Armory",
    "Mercenary Guild",
    "Bestiary",
    "Luxury",
    # "Slave Market",
)

towns_names = (
    "Aibiusa",
    "Zebrige",
    "Anosi",
    "Vleles",
    "Brario",
    "Strover",
    "Beksburg",
    "Zheocester",
)

roadsMatrix = (
#    1  2  3  4  5  6  7  8
    (0, 5, 1, 0, 4, 1, 0, 0),              # Aibiusa (1)
    (5, 0, 1, 0, 0, 0, 3, 0),              # Zebrige (2)
    (1, 1, 0, 0, 3, 0, 0, 0),              # Anosi (3)
    (0, 0, 0, 0, 4, 0, 0, 2),              # Vleles (4)
    (4, 0, 3, 4, 0, 0, 0, 0),              # Brario (5)
    (1, 0, 0, 0, 0, 0, 4, 3),              # Strover (6)
    (0, 3, 0, 0, 0, 4, 0, 0),              # Beksburg (7)
    (0, 0, 0, 2, 0, 3, 0, 0),              # Zheocester (8)
)
