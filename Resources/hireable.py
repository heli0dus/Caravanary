from Unit.Unit import Mercenary

hireable_dictionary = {
    # generator, description, size,  cost
    # "Week Employee": (0, 10),
    "Rookie": (Mercenary.rookie_generator, "", 0, 15),
    "Defender": (Mercenary.defender_generator, "", 0, 30),
    "Soldier": (Mercenary.soldier_generator, "", 0, 30),
    "Guardian": (Mercenary.guardian_generator, "", 0, 50),
    "Assasin": (Mercenary.assassin_generator, "", 0, 50),
    "Hero": (Mercenary.hero_generator, "", 0, 50),
    "Ultimate": (Mercenary.ultimate_generator, "", 0, 100),
}

hireable_variability = len(hireable_dictionary)

# TODO descriptions
# TODO more goods
