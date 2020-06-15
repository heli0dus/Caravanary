import random as rnd


class PlayerCaravan:
    name = ""
    money = 0
    to_pay = 0
    debt = 0
    debt_inc = 0
    human_food = 0
    animal_food = 0
    caravan_capacity = 0
    animal_size = 0
    human_size = 1
    employee_size = 0
    employee_set = set()
    mercenary_size = 0
    mercenary_set = set()
    worker_size = 0
    worker_set = set()
    warrior_size = 0
    warrior_set = set()
    location = ""

    def fight(self, enemies, player):
        player_in = ""
        print("Do ypu want to fight? yes/no: ")
        while player_in not in ["yes", "no"]:
            player_in = input()
            if player_in not in ["yes", "no"]:
                print("wrong command, try again")
            elif player_in == "yes":
                print("You stand to defend your caravan with your mercenaries")
                self.mercenary_set.union(player)
            else:
                print("You hide somewhere to protect your life")

        if isinstance(enemies, set):
            while len(self.mercenary_set.union()) > 0 and len(enemies) > 0:
                for i in self.mercenary_set.union(enemies):
                    if i.is_alive():
                        if i in self.mercenary_set:
                            i.hit(rnd.choice(tuple(enemies)))
                        else:
                            i.hit(rnd.choice(tuple(self.mercenary_set)))
                for i in list(self.mercenary_set):
                    if not i.is_alive():
                        self.mercenary_set.remove(i)

                for i in list(enemies):
                    if not i.is_alive():
                        enemies.remove(i)
            return len(self.mercenary_set) > 0
        else:
            print("Wrong argument of enemies given")

# TODO      trade function
# TODO      movement function
# TODO      leveling
# TODO      equipment
# TODO      refactor imports
