import Resources.tradeable_goods as dictionaries
import Resources.names as names
import Resources.tradeable_goods as tradeable_goods
import EconomicModule.TradePoint


class PlayerCaravan:
    name = ""               # Caravan's name given by player
    money = 20              # Current amount of money
    to_pay = 0              # Amount of money spending on caravan per day
    debt = 0                # Current money debt
    debt_inc = 0            # Multiplier applied to debt every 7 days
    human_food = 0          # Supply of food for humans
    human_food_open = 0     # Supply of food for humans that cant be sold
    animal_food = 0         # Supply of food for animals
    animal_food_open = 0    # Supply of food for animals that cant be sold
    caravan_capacity = 0    # Capacity of caravan, always <= 0
    capacity_current = 5    # Shown current capacity, sum of positive numbers
    capacity_maximum = 5    # Shown maximum of capacity, sum of negative numbers
    items_map = {"Silver dishes": 5,}          # Map of names and numbers of goods
    animal_size = 0         # Number of animals in caravan
    human_size = 1          # Number of humans in caravan (including player's character)
    mercenary_size = 0      # Number of mercenaries in caravan
    mercenary_set = set()   # Set of mercenaries
    location = "One"           # Name of current location
    # employee_size = 0       # Number of employee in caravan
    # employee_set = set()    # Set of employee
    # worker_size = 0         # Number of slaves-workers in caravan
    # worker_set = set()      # Set of slaves-workers
    # warrior_size = 0        # Number of slaves-warriors in caravan
    # warrior_set = set()     # Set of slaves-warriors

    def set_name(self, name):
        self.name = name

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
    # def caravan_get_mercenarys(self):
    # TODO printing mercenaries list
    # TODO fire mercenary
    # TODO drive the animal away
    # TODO slaughter an animal


#   Function to turn goods into money by goods_name or character name as goods_name
    def sell_item(self, goods_name, point):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if (self.items_map[goods_name] > 0) or (goods_name in self.items_map.keys()):
                thing = tradeable_goods.tradeable_goods[goods_name]
                if thing[0] == "hireable":
                    print("> You can't sell you mercenaries!")
                elif thing[0] == "animal":
                    if point.point_type != "Bestiary":
                        print("> I won't buy this.")
                    else:
                        if self.caravan_capacity-thing[-2] > 0:
                            print("> Then you can't carry so much!")
                        else:
                            self.caravan_capacity -= thing[-2]
                            if thing[-2] > 0:
                                self.capacity_current -= thing[-2]
                            else:
                                self.capacity_maximum += thing[-2]
                            earned = thing[-1]*point.specialization_multipliers[7]*point.richness_multipliers[7]
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
                    print("You buying some mercenaries!")
                    # TODO buy for mercenaries
                elif thing[0] == "animal":
                    if point.point_type != "Bestiary":
                        print("> I don't have " + goods_name + ", here isn't Bestiary!")
                    else:
                        if self.money >= point.goods_map[goods_name]:
                            if self.caravan_capacity+thing[-2] > 0:
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
                                self.items_map[goods_name] += 1
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
                            self.items_map[goods_name] += 1
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
                            self.items_map[goods_name] += 1
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
                            self.items_map[goods_name] += 1
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
                            self.items_map[goods_name] += 1
                        else:
                            print("> You have not enough money!")
            else:
                print("> I don't have ", goods_name, ", ask something other.")

    def buy_multi_item(self, goods_name, point, number):
        if isinstance(point, EconomicModule.TradePoint.TradePoint):
            if goods_name in point.goods_map.keys():
                if self.money >= point.goods_map[goods_name]*number:
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

#     def caravan_move(self, target):
# TODO      movement function
# TODO      trade functions (in progress)
# TODO      leveling
# TODO      equipment


