import Resources.tradeable_goods as dictionaries
import Resources.names as names
import Resources.animals
import Resources.human_food
import Resources.tradeable_goods as tradeable_goods
import EconomicModule.TradePoint
import random as rnd
import Unit.Unit
import Resources.towns_and_roads
import EconomicModule.Town as Town


class PlayerCaravan:
    name = ""  # Caravan's name given by player
    player_unit = Unit.Unit.Player()  # Player Unit
    money = 300  # Current amount of money
    to_pay = 0  # Amount of money spending on caravan per day
    debt = 0  # Current money debt
    debt_inc = 0  # Multiplier applied to debt every 7 days
    human_food = 0  # Supply of food for humans
    human_food_open = 0  # Supply of food for humans that cant be sold
    animal_food = 0  # Supply of food for animals
    animal_food_open = 0  # Supply of food for animals that cant be sold
    caravan_capacity = -5  # Capacity of caravan, always <= 0
    capacity_current = 0  # Shown current capacity, sum of positive numbers
    capacity_maximum = 5  # Shown maximum of capacity, sum of negative numbers
    items_map = {}  # Map of names and numbers of goods
    animal_size = 0  # Number of animals in caravan
    human_size = 1  # Number of humans in caravan (including player's character)
    mercenary_size = 0  # Number of mercenaries in caravan
    mercenary_set = set()  # Set of mercenaries
    location = "Aibiusa"  # Name of current location
    day = 0
    point = EconomicModule.TradePoint.TradePoint(Town.real_towns_names[location], "Armory")
    state_commands = {}

    # employee_size = 0       # Number of employee in caravan
    # employee_set = set()    # Set of employee
    # worker_size = 0         # Number of slaves-workers in caravan
    # worker_set = set()      # Set of slaves-workers
    # warrior_size = 0        # Number of slaves-warriors in caravan
    # warrior_set = set()     # Set of slaves-warriors

    def set_name(self, name):
        self.name = name

    def set_commands(self, com_dict):
        self.state_commands = com_dict

    def set_point(self, point):
        self.point = point

    def add_money(self, amount):
        self.money += amount
        print("Cheat used")

    def add_human_food(self, amount):
        self.human_food_open += 100
        print("cheat used")

    def add_animal_food(self, amount):
        self.animal_food_open += 100
        print("cheat used")

    # Shows money, food, capacity and size
    def get_info(self):
        print()
        print("Your caravan info: ", self.name)
        print(" vvv ")
        print("   Now you are in town", self.location)
        print("   Money: ", self.money, ", where debt is: ", self.debt)
        print("   Paying mercenaries per day: ", self.to_pay)
        print("   Capacity: ", self.capacity_current, "/", self.capacity_maximum)
        print("   Number of animals: ", self.animal_size)
        print("   Number of humans: ", self.human_size)
        print("   Food: for humans:  ", self.human_food_open, "(+", self.human_food, ")")
        print("         for animals: ", self.animal_food_open, "(+", self.animal_food, ")")
        print(" ^^^ ")
        print()

    # Shows list of items in inventory
    def get_items(self):
        if self.items_map.__len__() != 0:
            print()
            print("You have these items in your inventory: ")
            print(" vvv ")
            for i in self.items_map.keys():
                print("   ", i, ": ", self.items_map[i])
            print(" ^^^ ")
            print()
        else:
            print("Your inventory is empty.")

    # Shows set of mercenarys
    def get_mercenarys(self):

        if len(self.mercenary_set) > 0:
            l = list(self.mercenary_set)
            for i in range(len(l)):
                print(i)
                l[i].print()
        else:
            print("You don't have any mercenaries.")

    def fire_mercenary(self, mercenary):
        self.to_pay -= mercenary.salry
        self.mercenary_size -= 1
        self.human_size -= 1
        self.mercenary_set.remove(mercenary)

    # TODO daily update method

    # Allows to delete animal from caravan
    def drive_out_animal(self, animal_name):
        if animal_name in Resources.animals.animals_dictionary:
            if animal_name in self.items_map.keys() and self.items_map[animal_name] > 0:
                if tradeable_goods.tradeable_goods[animal_name][-2] < 0:
                    if self.caravan_capacity - tradeable_goods.tradeable_goods[animal_name][-2] <= 0:
                        self.caravan_capacity -= tradeable_goods.tradeable_goods[animal_name][-2]
                        self.capacity_maximum -= tradeable_goods.tradeable_goods[animal_name][-2]
                        self.animal_size -= 1
                        self.items_map[animal_name] -= 1
                    else:
                        print("You can't do this, you have not enough capacity.")
                else:
                    self.caravan_capacity -= tradeable_goods.tradeable_goods[animal_name][-2]
                    self.capacity_current -= tradeable_goods.tradeable_goods[animal_name][-2]
                    self.animal_size -= 1
                    self.items_map[animal_name] -= 1
            else:
                print("You have no such animal")
        else:
            print("This is not an animal")

    def slautgher_animal(self, animal_name):
        if animal_name in Resources.animals.animals_dictionary:
            if animal_name in self.items_map.keys() and self.items_map[animal_name] > 0:
                if tradeable_goods.tradeable_goods[animal_name][-2] < 0:
                    if self.caravan_capacity - tradeable_goods.tradeable_goods[animal_name][-2] <= 0:
                        self.caravan_capacity -= tradeable_goods.tradeable_goods[animal_name][-2]
                        self.capacity_maximum -= tradeable_goods.tradeable_goods[animal_name][-2]
                        self.human_food_open += tradeable_goods.tradeable_goods[animal_name][2]
                        self.animal_size -= 1
                        self.items_map[animal_name] -= 1
                    else:
                        print("You can't do this, you have not enough capacity.")
                else:
                    self.caravan_capacity -= tradeable_goods.tradeable_goods[animal_name][-2]
                    self.capacity_current -= tradeable_goods.tradeable_goods[animal_name][-2]
                    self.human_food_open += tradeable_goods.tradeable_goods[animal_name][2]
                    self.animal_size -= 1
                    self.items_map[animal_name] -= 1
            else:
                print("You have no such animal")
        else:
            print("This is not an animal")

    def open_human_food(self, need):
        flag = False
        opened = 0
        while not flag:
            flag_feeded = True
            flag_take_more = False
            for i in self.items_map:
                if tradeable_goods.tradeable_goods[i][0] == "human_food" and self.items_map[i] > 0:
                    if opened > need:
                        flag = True
                    if tradeable_goods.tradeable_goods[i][1] <= opened - need:
                        self.human_food_open += tradeable_goods.tradeable_goods[i][1]
                        self.human_food -= tradeable_goods.tradeable_goods[i][1]
                        opened += tradeable_goods.tradeable_goods[i][1]
                        self.items_map[i] -= 1
                        flag_take_more = True
            if not flag_take_more:
                flag_feeded = False
                for i in self.items_map:
                    if tradeable_goods.tradeable_goods[i][0] == "human_food" and self.items_map[i] > 0:
                        if tradeable_goods.tradeable_goods[i][1] >= opened - need:
                            self.human_food_open += tradeable_goods.tradeable_goods[i][1]
                            self.human_food -= tradeable_goods.tradeable_goods[i][1]
                            opened += tradeable_goods.tradeable_goods[i][1]
                            self.items_map[i] -= 1
                            flag_feeded = True

            if not flag_feeded:
                flag = False
                break

        if not flag:
            return "You don't have enough food."
        return "fine"

    def open_animal_food(self, need):
        flag = False
        opened = 0
        while not flag:
            flag_feeded = True
            flag_take_more = False
            for i in self.items_map:
                if i[0] == "animal_food" and self.items_map[i] > 0:
                    if i[1] <= opened - need:
                        self.animal_food_open += i[1]
                        opened += i[1]
                        self.items_map[i] -= 1
                        flag_take_more = True
            if not flag_take_more:
                flag_feeded = False
                for i in self.items_map:
                    if i[0] == "animal_food" and self.items_map[i] > 0:
                        if i[1] >= opened - need:
                            self.animal_food_open += i[1]
                            opened += i[1]
                            self.items_map[i] -= 1
                            flag_feeded = True

            if not flag_feeded:
                flag = False
                break

        if not flag:
            return "You don't have enough food."
        return "fine"

    #   Function to turn goods into money by goods_name or character name as goods_name
    def sell_item(self, goods_name, point):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if (goods_name in self.items_map.keys()) and (self.items_map[goods_name] > 0):
                thing = tradeable_goods.tradeable_goods[goods_name]
                if thing[0] == "hireable":
                    print("> You can't sell you mercenaries!")
                elif thing[0] == "animal":
                    if point.point_type != "Bestiary":
                        print("> I won't buy this.")
                    else:
                        if self.caravan_capacity - thing[-2] > 0:
                            print("> Then you can't carry so much!")
                        else:
                            self.caravan_capacity -= thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current -= thing[-2]
                            else:
                                self.capacity_maximum += thing[-2]
                            earned = thing[-1] * point.specialization_multipliers[7] * point.richness_multipliers[7]
                            print("Earned: ", earned, ".")
                            self.money += earned
                            self.animal_size -= 1
                            self.items_map[goods_name] -= 1
                elif thing[0] == "armor":
                    if point.point_type != "Armory":
                        print("I won't buy this.")
                    else:
                        self.caravan_capacity -= thing[-2]
                        if thing[-2] > 0:
                            self.capacity_current -= thing[-2]
                        else:
                            self.capacity_maximum += thing[-2]
                        earned = thing[-1] * point.specialization_multipliers[3] * point.richness_multipliers[3]
                        print("Earned: ", earned, ".")
                        self.money += earned
                        self.items_map[goods_name] -= 1
                elif thing[0] == "animal_food":
                    if point.point_type != "Market":
                        print("> I won't buy this.")
                    else:
                        self.caravan_capacity -= thing[-2]
                        if thing[-2] > 0:
                            self.capacity_current -= thing[-2]
                        else:
                            self.capacity_maximum += thing[-2]
                        earned = thing[-1] * point.specialization_multipliers[1] * point.richness_multipliers[1]
                        print("Earned: ", earned, ".")
                        self.money += earned
                        self.animal_food -= thing[1]
                        self.items_map[goods_name] -= 1
                elif thing[0] == "human_food":
                    if point.point_type != "Market":
                        print("> I won't buy this.")
                    else:
                        self.caravan_capacity -= thing[-2]
                        if thing[-2] > 0:
                            self.capacity_current -= thing[-2]
                        else:
                            self.capacity_maximum += thing[-2]
                        earned = thing[-1] * point.specialization_multipliers[0] * point.richness_multipliers[0]
                        print("Earned: ", earned, ".")
                        self.money += earned
                        self.human_food -= thing[1]
                        self.items_map[goods_name] -= 1
                elif thing[0] == "luxury":
                    if point.point_type != "Luxury":
                        print("> I won't buy this.")
                    else:
                        self.caravan_capacity -= thing[-2]
                        if thing[-2] > 0:
                            self.capacity_current -= thing[-2]
                        else:
                            self.capacity_maximum += thing[-2]
                        earned = thing[-1] * point.specialization_multipliers[4] * point.richness_multipliers[4]
                        print("Earned: ", earned, ".")
                        self.money += earned
                        self.items_map[goods_name] -= 1
                elif thing[0] == "weapon":
                    if point.point_type != "Armory":
                        print("> I won't buy this.")
                    else:
                        self.caravan_capacity -= thing[-2]
                        if thing[-2] > 0:
                            self.capacity_current -= thing[-2]
                        else:
                            self.capacity_maximum += thing[-2]
                        earned = thing[-1] * point.specialization_multipliers[2] * point.richness_multipliers[2]
                        print("Earned: ", earned, ".")
                        self.money += earned
                        self.items_map[goods_name] -= 1
            else:
                print("there is no such item")
        else:
            print("> You don't have " + goods_name + " in your inventory.")

    def sell_multi_item(self, goods_name, point, number):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if goods_name in self.items_map.keys():
                if self.items_map[goods_name] >= number:
                    thing = tradeable_goods.tradeable_goods[goods_name]
                    if thing[0] == "animal_food" or thing[0] == "human_food":
                        if point.point_type == "Market":
                            for i in range(number):
                                PlayerCaravan.sell_item(self, goods_name, point)
                            print("Sold: ", number, goods_name, ".")
                        else:
                            print("> I won't buy this.")
                    elif thing[0] == "animal":
                        if point.point_type == "Bestiary":
                            for i in range(number):
                                PlayerCaravan.sell_item(self, goods_name, point)
                            print("Sold: ", number, goods_name, ".")
                        else:
                            print("> I won't buy this.")
                    elif thing[0] == "armor" or thing[0] == "weapon":
                        if point.point_type == "Armory":
                            for i in range(number):
                                PlayerCaravan.sell_item(self, goods_name, point)
                            print("Sold: ", number, goods_name, ".")
                        else:
                            print("> I won't buy this.")
                    elif thing[0] == "hireable":
                        print("> You can't sell you mercenaries!")
                    elif thing[0] == "luxury":
                        if point.point_type == "Luxury":
                            for i in range(number):
                                PlayerCaravan.sell_item(self, goods_name, point)
                            print("Sold: ", number, goods_name, ".")
                        else:
                            print("> I won't buy this.")
                else:
                    print("> You have not enough " + goods_name + ".")
            else:
                print("> You don't have ", goods_name, ".")

    def buy_item(self, goods_name, point):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if goods_name in point.goods_map.keys():
                thing = tradeable_goods.tradeable_goods[goods_name]
                if thing[0] == "hireable":
                    if point.point_type != "Mercenary Guild":
                        print("> You buying some mercenaries! It's not here!")
                    else:
                        if self.money >= point.goods_map[goods_name][1]:
                            print("Payed: ", point.goods_map[goods_name][1])
                            self.money -= point.goods_map[goods_name][1]
                            self.mercenary_size += 1
                            self.to_pay += point.goods_map[goods_name][0].salary
                            self.human_size += 1
                            self.mercenary_set.add(point.goods_map[goods_name][0])
                            del point.goods_map[goods_name]
                elif thing[0] == "animal":
                    if point.point_type != "Bestiary":
                        print("> I don't have " + goods_name + ", here isn't Bestiary!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            if self.caravan_capacity + thing[-2] > 0:
                                print("> You can't carry so much!")
                            else:
                                self.caravan_capacity += thing[-2]
                                if thing[-2] > 0:
                                    self.capacity_current += thing[-2]
                                else:
                                    self.capacity_maximum -= thing[-2]
                                print("Payed: ", point.goods_map[goods_name])
                                self.money -= point.goods_map[goods_name]
                                self.animal_size += 1
                                if goods_name in self.items_map:
                                    self.items_map[goods_name] += 1
                                else:
                                    self.items_map[goods_name] = 1
                        else:
                            print("> You have not enough money!")
                elif thing[0] == "armor":
                    if point.point_type != "Armory":
                        print("> I don't have " + goods_name + ", here isn't Armory!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            self.caravan_capacity += thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current += thing[-2]
                            else:
                                self.capacity_maximum -= thing[-2]
                            print("Payed: ", point.goods_map[goods_name])
                            self.money -= point.goods_map[goods_name]
                            self.items_map[goods_name] -= 1
                        else:
                            print("> You have not enough money!")
                elif thing[0] == "animal_food":
                    if point.point_type != "Market":
                        print("> I don't have " + goods_name + ", here isn't Market!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            self.caravan_capacity += thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current += thing[-2]
                            else:
                                self.capacity_maximum -= thing[-2]
                            self.money -= point.goods_map[goods_name]
                            self.animal_food += thing[1]
                            if goods_name in self.items_map:
                                self.items_map[goods_name] += 1
                            else:
                                self.items_map[goods_name] = 1
                        else:
                            print("> You have not enough money!")
                elif thing[0] == "human_food":
                    if point.point_type != "Market":
                        print("> I don't have " + goods_name + ", here isn't Market!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            self.caravan_capacity += thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current += thing[-2]
                            else:
                                self.capacity_maximum -= thing[-2]
                            print("Payed: ", point.goods_map[goods_name])
                            self.money -= point.goods_map[goods_name]
                            self.human_food += thing[1]
                            if goods_name in self.items_map:
                                self.items_map[goods_name] += 1
                            else:
                                self.items_map[goods_name] = 1
                        else:
                            print("> You have not enough money!")
                elif thing[0] == "luxury":
                    if point.point_type != "Luxury":
                        print("> I don't have " + goods_name + ", here isn't Luxury shop!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            self.caravan_capacity += thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current += thing[-2]
                            else:
                                self.capacity_maximum -= thing[-2]
                            print("Payed: ", point.goods_map[goods_name])
                            self.money -= point.goods_map[goods_name]
                            if goods_name in self.items_map:
                                self.items_map[goods_name] += 1
                            else:
                                self.items_map[goods_name] = 1
                        else:
                            print("> You have not enough money!")
                elif thing[0] == "weapon":
                    if point.point_type != "Armory":
                        print("> I don't have " + goods_name + ", here isn't Armory!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            self.caravan_capacity += thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current += thing[-2]
                            else:
                                self.capacity_maximum -= thing[-2]
                            print("Payed: ", point.goods_map[goods_name])
                            self.money -= point.goods_map[goods_name]
                            if goods_name in self.items_map:
                                self.items_map[goods_name] += 1
                            else:
                                self.items_map[goods_name] = 1
                        else:
                            print("> You have not enough money!")
            else:
                print("> I don't have ", goods_name, ", ask something other.")

    def buy_multi_item(self, goods_name, point, number):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if goods_name in point.goods_map.keys():
                if point.point_type == "Mercenary Guild":
                    tempint = point.goods_map[goods_name][1]
                else:
                    tempint = point.goods_map[goods_name]
                if self.money >= tempint * number:
                    thing = tradeable_goods.tradeable_goods[goods_name]
                    if thing[0] == "animal_food" or thing[0] == "human_food":
                        if point.point_type == "Market":
                            for i in range(number):
                                PlayerCaravan.buy_item(self, goods_name, point)
                            print("Purchased: ", number, goods_name, ".")
                        else:
                            print("> I don't have " + goods_name + ", here isn't Market!")
                    elif thing[0] == "animal":
                        if point.point_type == "Bestiary":
                            for i in range(number):
                                PlayerCaravan.buy_item(self, goods_name, point)
                            print("Purchased: ", number, goods_name, ".")
                        else:
                            print("> I don't have " + goods_name + ", here isn't Bestiary!")
                    elif thing[0] == "armor" or thing[0] == "weapon":
                        if point.point_type == "Armory":
                            for i in range(number):
                                PlayerCaravan.buy_item(self, goods_name, point)
                            print("Purchased: ", number, goods_name, ".")
                        else:
                            print("> I don't have " + goods_name + ", here isn't Armory!")
                    elif thing[0] == "hireable":
                        print("> You can't sell you mercenaries!")
                    elif thing[0] == "luxury":
                        if point.point_type == "Luxury":
                            for i in range(number):
                                PlayerCaravan.buy_item(self, goods_name, point)
                            print("Purchased: ", number, goods_name, ".")
                        else:
                            print("> I don't have " + goods_name + ", here isn't Luxury shop!")
                else:
                    print("> You have not enough money!")
            else:
                print("> I don't have ", goods_name, ", ask something other.")

    def fight(self, enemies):
        player_in = ""
        print("Do ypu want to fight? yes/no: ")
        while player_in not in ["yes", "no"]:
            player_in = input()
            if player_in not in ["yes", "no"]:
                print("wrong command, try again")
            elif player_in == "yes":
                print("You stand to defend your caravan with your mercenaries")
                fighting_set = set(self.mercenary_set.union({self.player_unit}))
            else:
                fighting_set = set(self.mercenary_set)
                print("You hide somewhere to protect your life")

        if isinstance(enemies, set):
            while len(fighting_set) > 0 and len(enemies) > 0:
                for i in fighting_set.union(enemies):
                    if i.is_alive():
                        if i in fighting_set:
                            i.hit(rnd.choice(tuple(enemies)))
                        else:
                            i.hit(rnd.choice(tuple(fighting_set)))
                for i in list(fighting_set):
                    if not i.is_alive():
                        self.mercenary_set.remove(i)
                        fighting_set.remove(i)

                for i in list(enemies):
                    if not i.is_alive():
                        enemies.remove(i)
            return len(fighting_set) <= 0
        else:
            print("Wrong argument of enemies given")

    def caravan_move(self, target):
        now = EconomicModule.Town.get_town_index(Town.real_towns_names[self.location])
        target = EconomicModule.Town.get_town_index(Town.real_towns_names[target])
        if Resources.towns_and_roads.roadsMatrix[now][target] > 0:
            self.location = EconomicModule.Town.town_by_index(target)
            return Resources.towns_and_roads.roadsMatrix[now][target]
        else:
            print("There is no road to this town.")
            return 0

    def next_day(self):
        Town.real_towns_names[self.location].re_generate_points()
        self.day += 1
        result = False
        for i in list(self.mercenary_set):
            if self.money < i.salary and not result:
                print(i.name + " kills you for not paying money. Don't keep merenaries if you can't pay them")
                result = True
            else:
                self.money -= i.salary
        if self.human_food_open - self.human_size < 0:
            feed_human = self.open_human_food(-(self.human_food_open - self.human_size))
            if feed_human == "You don't have enough food." and not result:
                print("You died of starvation. Keep an eye on your food balance")
                result = True
        else:
            self.human_food_open -= self.human_size
        if self.animal_food_open - self.animal_size < 0:
            feed_animal = self.open_animal_food(-(self.animal_food_open - self.animal_size))
            if feed_animal == "You don't have enough food." and not result:
                print("Your animals ran away with all the goods. You hang yourself in the nearest tree")
            result = True
            self.animal_food_open -= self.animal_size
        else:
            self.animal_food_open -= self.animal_size
        return result
# TODO      leveling
# TODO      equipment
