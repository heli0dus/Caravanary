armor_dictionary = {
    # armor, evade chance, description, size, cost
    "Light leather armor": (3, -2, "", 1, 15),
    "Leather armor": (5, -5, "", 1, 20),
    "Iron armor": (10, -10, "", 1, 30),
    "Fortified leather armor": (8, -5, "", 1, 30),
    "Steel armor": (12, -15, "", 1, 45),
    "Valit armor": (18, -10, "", 1, 120),
    "Plate vest": (20, -20, "", 1, 150),
    "Kaom's Heart": (30, -30, "", 1, 300),
    "none": (0, 0, "", 0, 0),
}
# mercenaries
rookie = {
    "Light leather armor": (3, -2, "", 1, 15),
}

defender = {
    "Iron armor": (10, -10, "", 1, 30),
}

soldier = {
    "Iron armor": (10, -10, "", 1, 30),
    "Fortified leather armor": (8, -5, "", 1, 30),
}

guardian = {
    "Steel armor": (12, -15, "", 1, 45),
    "Iron armor": (10, -10, "", 1, 30),
    "Valit armor": (18, -10, "", 1, 120),
}

assassin = {
    "Iron armor": (10, -10, "", 1, 30),
    "Fortified leather armor": (8, -5, "", 1, 30),
}

hero = {
    "Steel armor": (12, -15, "", 1, 45),
    "Valit armor": (18, -10, "", 1, 120),
    "Plate vest": (20, -20, "", 1, 150),
}

ultimate = {
    "Fortified leather armor": (8, -5, "", 1, 30),
    "Valit armor": (18, -10, "", 1, 120),
    "Plate vest": (20, -20, "", 1, 150),
    "Kaom's Heart": (30, -30, "", 1, 300),
}

# bandits
thief = {
    "Light leather armor": (3, -2, "", 1, 15),
}

pickpocket = {
    "Light leather armor": (3, -2, "", 1, 15),
    "Leather armor": (5, -5, "", 1, 20),
}

archer = {
    "Leather armor": (5, -5, "", 1, 20),
}

bouncer = {
    "Iron armor": (10, -10, "", 1, 30),
    "Fortified leather armor": (8, -5, "", 1, 30),
}

deserter = {
    "Iron armor": (10, -10, "", 1, 30),
    "Steel armor": (12, -15, "", 1, 45),
}

killer = {
    "Fortified leather armor": (8, -5, "", 1, 30),
    "Valit armor": (18, -10, "", 1, 120),
}

leader = {
    "Steel armor": (12, -15, "", 1, 45),
    "Valit armor": (18, -10, "", 1, 120),
    "Plate vest": (20, -20, "", 1, 150),
}

armor_variability = len(armor_dictionary)

# TODO descriptions
