import Resources.tradeable_goods as dictionaries
import Resources.names as names


class PlayerCaravan:
    name = ""               # Caravan's name given by player
    money = 0               # Current amount of money
    to_pay = 0              # Amount of money spending on caravan per day
    debt = 0                # Current money debt
    debt_inc = 0            # Multiplier applied to debt every 7 days
    human_food = 0          # Supply of food for humans
    animal_food = 0         # Supply of food for animals
    caravan_capacity = 0    # Capacity of caravan, always <= 0
    capacity_current = 0    # Shown current capacity, sum of positive numbers
    capacity_maximum = 0    # Shown maximum of capacity, sum of negative numbers
    items_map = {}          # Map of names and numbers of goods
    animal_size = 0         # Number of animals in caravan
    human_size = 1          # Number of humans in caravan (including player's character)
    employee_size = 0       # Number of employee in caravan
    employee_set = set()    # Set of employee
    mercenary_size = 0      # Number of mercenaries in caravan
    mercenary_set = set()   # Set of mercenaries
    worker_size = 0         # Number of slaves-workers in caravan
    worker_set = set()      # Set of slaves-workers
    warrior_size = 0        # Number of slaves-warriors in caravan
    warrior_set = set()     # Set of slaves-warriors
    location = ""           # Name of current location

#   Function to turn goods into money by goods_name or character name as goods_name
#     def caravan_sell(self, goods_name, point):
#         if self.items_map[goods_name] > 0:
#             for DICT in dictionaries.dictionaries:
#                 if goods_name in DICT:
#                     if DICT == dictionaries.dictionaries[1]:
#                         # TODO "sell" for animals
#                     elif DICT == dictionaries.dictionaries[3]:
#                         # TODO "sell" for food
#                     elif DICT == dictionaries.dictionaries[4]:
#                         # TODO "sell" for hireable
#                     elif DICT == dictionaries.dictionaries[6]:
#                         # TODO "sell" for slaves
#                     else:
#                         self.items_map[goods_name] -= 1
#                         self.caravan_capacity -= DICT[goods_name][-2]
#                         self.money += DICT[goods_name][-1]
#                         # TODO TradePoint multiplier for "sell"
#                 else:
#                     print("What is that thing?")
#         else:
#             print("You don't have " + goods_name + " in your inventory")

#     def caravan_move(self, target):
# # TODO      movement function


# TODO      trade functions (in progress)
# TODO      leveling
# TODO      equipment
# TODO      refactor imports
