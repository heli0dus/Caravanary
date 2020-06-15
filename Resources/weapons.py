weapon_dictionary = {
    # lower damage, higher damage, accuracy, description, size, cost
    "Axe": (10, 20, 20, "", 1, 30),
    "Sword": (7, 15, 30, "", 1, 25),
    "Light axe": (5, 15, 25, "", 1, 20),
    "Dagger": (3, 10, 50, "", 1, 15),
    "Spear": (5, 20, 45, "", 1, 50),
    "Halberd": (15, 25, 35, "", 1, 50),
    "Twinblade": (15, 40, 45, "", 1, 90),
    "Flamberg": (25, 40, 35, "", 1, 110),
    "Frostmourne": (30, 50, 40, "", 1, 250),
    "none": (0, 0, 0, "", 0, 0)
}

# mercenaries
rookie = {
    "Light axe": (5, 15, 40, "", 1, 20),
}

defender = {
    "Axe": (10, 20, 20, "", 1, 30),
    "Sword": (7, 15, 30, "", 1, 25)
}

soldier = {
    "Dagger": (3, 10, 50, "", 1, 15),
    "Spear": (5, 20, 45, "", 1, 50),
}

guardian = {
    "Dagger": (3, 10, 50, "", 1, 15),
    "Spear": (5, 20, 45, "", 1, 50),
}

assassin = {
    "Spear": (5, 20, 45, "", 1, 50),
    "Halberd": (15, 25, 35, "", 1, 50),
}

hero = {
    "Spear": (5, 20, 45, "", 1, 50),
    "Halberd": (15, 25, 35, "", 1, 50),
    "Twinblade": (15, 40, 45, "", 1, 70),
    "Flamberg": (25, 40, 35, "", 1, 110),
}

ultimate = {
    "Twinblade": (15, 40, 45, "", 1, 90),
    "Flamberg": (25, 40, 35, "", 1, 110),
    "Frostmourne": (30, 50, 40, "", 1, 250),
}

# bandits
thief = {
    "Dagger": (3, 10, 50, "", 1, 15),
}

pickpocket = {
    "Dagger": (3, 10, 50, "", 1, 15),
    "Sword": (7, 15, 30, "", 1, 25),
}

archer = {
    "Light axe": (5, 15, 25, "", 1, 20),
    "Dagger": (3, 10, 50, "", 1, 15),
    "Spear": (5, 20, 45, "", 1, 50),
}

bouncer = {
    "Axe": (10, 20, 20, "", 1, 30),
    "Sword": (7, 15, 30, "", 1, 25),
}

deserter = {
    "Spear": (5, 20, 45, "", 1, 50),
    "Halberd": (15, 25, 35, "", 1, 50),
}

killer = {
    "Halberd": (15, 25, 35, "", 1, 50),
    "Flamberg": (25, 40, 35, "", 1, 110),
}

leader = {
    "Spear": (5, 20, 45, "", 1, 50),
    "Twinblade": (15, 40, 45, "", 1, 90),
    "Halberd": (15, 25, 35, "", 1, 50),
    "Flamberg": (25, 40, 35, "", 1, 110),
}

weapon_variability = len(weapon_dictionary)

# TODO descriptions
