from EconomicModule import *
from Unit import Unit
from Resources import *
import random as rnd

print("Initializing resources")
tradeable_goods.collect_all_goods()
caravan = PlayerCaravan.PlayerCaravan()
leave = False


def show_directions():
    search_tuple = towns_and_roads.roadsMatrix[Town.get_town_index(Town.real_towns_names[caravan.location])]
    for i in range(len(search_tuple)):
        if search_tuple[i] > 0:
            print(Town.town_by_index(i), search_tuple[i], "days")


def choose_point(num):
    if num <= len(Town.real_towns_names[caravan.location].points):
        caravan.point = Town.real_towns_names[caravan.location].points[num]
        caravan.set_commands(trade_commands)
    else:
        print("There is no point with such number")


def move():
    target = input("Where do you want to move? ")
    if target in towns_and_roads.towns_names:
        length = caravan.caravan_move(target)
        dead = False
        for i in range(length):
            if not dead:
                dead = road_travel()
        return dead
    else:
        print("There is no such city")


def nothing():
    dead = False
    print("You peacefully passed this day")
    dead = caravan.next_day()
    return dead


def bandit_death_finish():
    print("Bandits kiiled you. What a good death for such a good person. Game over")
    return True


def bandit_capture_finish():
    print("bandits killed everybody in your caravan. Now you are their slave. game over")
    return True


def small_gang_attack():
    size = (caravan.human_size + caravan.animal_size) // 2 + rnd.randint(-2, 2)
    attackers = set()
    for i in range(size // 2):
        attackers.add(Unit.Unit.thief_generator())
        attackers.add(Unit.Unit.pickpocket_generator())
    attackers.add(Unit.Unit.archer_generator())
    print("Small gang approaches you. prepare to fight!")
    lose = caravan.fight(attackers)
    if lose:
        bandit_death_finish()
    elif caravan.player_unit.is_alive():
        print("That small gang is dead")
        return caravan.next_day()
    else:
        return bandit_death_finish()


def med_gang_attack():
    size = (caravan.human_size + caravan.animal_size) // 2 + rnd.randint(-1, 3)
    attackers = set()
    for i in range(size // 2):
        attackers.add(Unit.Unit.archer_generator())
        attackers.add(Unit.Unit.bouncer_generator())
    attackers.add(Unit.Unit.deserter_generator())
    print("A gang approaches you. prepare to fight!")
    lose = caravan.fight(attackers)
    if lose:
        bandit_death_finish()
    elif caravan.player_unit.is_alive():
        print("That gang is dead")
        return caravan.next_day()
    else:
        return bandit_death_finish()


def strong_gang_attack():
    size = (caravan.human_size + caravan.animal_size) // 2 + rnd.randint(0, 4)
    attackers = set()
    for i in range(size // 2):
        attackers.add(Unit.Unit.deserter_generator())
        attackers.add(Unit.Unit.killer_generator())
    attackers.add(Unit.Unit.leader_generator())
    print("Strong gang approaches you. Prepare to fight!")
    lose = caravan.fight(attackers)
    if lose:
        bandit_death_finish()
    elif caravan.player_unit.is_alive():
        print("One more big gang was destroyed today")
        return caravan.next_day()
    else:
        return bandit_death_finish()


def road_travel():
    russian_roulette = [[nothing,
                         nothing,
                         nothing,
                         nothing,
                         nothing,
                         nothing,
                         nothing,
                         nothing,
                         small_gang_attack,
                         small_gang_attack,
                         small_gang_attack,
                         small_gang_attack,
                         med_gang_attack,
                         med_gang_attack,
                         strong_gang_attack
                         ],
                        [nothing,
                         nothing,
                         nothing,
                         nothing,
                         small_gang_attack,
                         med_gang_attack,
                         med_gang_attack,
                         strong_gang_attack
                         ],
                        [nothing,
                         nothing,
                         med_gang_attack,
                         med_gang_attack,
                         strong_gang_attack
                         ],
                        [nothing,
                         strong_gang_attack
                         ]]
    return rnd.choice(russian_roulette[caravan.day // 7 % 4])()


def trade():
    caravan.state_commands = trade_choose_commands
    print("You see some tradepoints:")
    Town.real_towns_names[caravan.location].print_points()
    print("Choose a point number:")


def print_commands():
    for i in caravan.state_commands.keys():
        print(i)
    for i in always_avialable.keys():
        print(i)


def quit_game():
    confirm = input("Are you sure? Y/n ")
    if confirm == "Y":
        print("Come again, hope ypu had fun!")
        return True
    elif confirm == "n":
        print("Good to hear")
        return False
    else:
        print("Unknown command")


def buy_something():
    item = input(">What do you want?\n")
    caravan.buy_item(item, caravan.point)


def sell_something():
    item = input(">What do you want?\n")
    caravan.sell_item(item, caravan.point)


cheats = {
    "BlueEyeBlond": (lambda: caravan.add_money(300)),
    "LEEEEROOOY": (lambda: caravan.mercenary_set.add(Unit.Mercenary.LEEEEROOOY())),
    "golden shower": (lambda: caravan.add_human_food(100)),
    "farmboy": (lambda: caravan.add_animal_food(100))
}

always_avialable = {
    "location": lambda: print(caravan.location),
    "commands": print_commands,
    "quit": quit_game,
    "day": lambda: print("Day "+str(caravan.day)),
    "help": lambda: print("First of all, tour target. You need to survive as long as you can\n"
                          "To keep your caravan you need to resell goods.\n"
                          "But you can increase your profit by reselling items in different cities\n"
                          "Each city has it's specialization and has higher or lower prices to certain goods\n"
                          "How to find city specialization? By looking at prices, we will not tell you :)"
                          "To move goods you can buy some animals. "
                          "They can be quite useful when you starve while travelling and they carry goods\n"
                          "Obviously, you have to eas something to live. "
                          "So don't forget to buy food for yourself, your workers and your animals\n"
                          "On roads you may meet some bandits and they don't like to keep people alive. "
                          "Hire some mercenaries.\n\n"
                          "And one last thing. If you forget anything simply type '/help' and we will try to clear "
                          "things up. Print 'commands' to see what you can do "
                          "Good luck!"),
    "get info": lambda: caravan.get_info(),
    "mercenaries": lambda: caravan.get_mercenarys(),
    "items": lambda: caravan.get_items(),
    "roads": show_directions
}

town_actions = {
    "stay": lambda: caravan.next_day(),
    "move": move,
    "trade": trade
}

trade_choose_commands = {
    '1': lambda: choose_point(0),
    '2': lambda: choose_point(1),
    '3': lambda: choose_point(2),
    '4': lambda: choose_point(3),
    '5': lambda: choose_point(4),
    '6': lambda: choose_point(5),
    '7': lambda: choose_point(6),
    '8': lambda: choose_point(7),
    '9': lambda: choose_point(8),
    '10': lambda: choose_point(9),
    '11': lambda: choose_point(10),
    '12': lambda: choose_point(11),
    'back': lambda: caravan.set_commands(town_actions)
}

trade_commands = {
    "what you have": lambda: print(caravan.point),
    "give me...": buy_something,
    "do you want...": sell_something,
    "nothing interesting": lambda: caravan.set_commands(trade_choose_commands),
    "I'm done": lambda: caravan.set_commands(trade_choose_commands)
}

print('Welcome to "Caravanary"')
print('You gained some money and now can make your dram of being a caravan master real!')
print('You\'ll gain some useful information later.')
name = input('Firstly, how do you want to name your caravan? ')
confirm = input("Do you really want to name your caravan " + name + "? Y/n ")

while confirm != "Y":
    if confirm != "n":
        confirm = input("Wrong command. Try again Y/n")
    else:
        name = input("Ok, enter another name:")
        confirm = input("Do you really want to name your caravan " + name + "? Y/n ")

caravan.set_name(name)
print("\nWhat a good name! And now, a short introduction to our game:\n")

print("First of all, tour target. You need to survive as long as you can\n"
      "To keep your caravan you need to resell goods.\n"
      "But you can increase your profit by reselling items in different cities\n"
      "Each city has it's specialization and has higher or lower prices to certain goods\n"
      "How to find city specialization? By looking at prices, we will not tell you :)"
      "To move goods you can buy some animals. "
      "They can be quite useful when you starve while travelling and they carry goods\n"
      "Obviously, you have to eas something to live. "
      "So don't forget to buy food for yourself, your workers and your animals\n"
      "On roads you may meet some bandits and they don't like to keep people alive. "
      "Hire some mercenaries.\n\n"
      "And one last thing. If you forget anything simply type '/help' and we will try to clear things up. "
      "Good luck! Print 'commands' to see what you can do")

caravan.state_commands = town_actions

while not leave:
    command = input("$ ")
    result = False
    if command in always_avialable:
        result = always_avialable[command]()
    elif command in cheats:
        result = cheats[command]()
    elif command in caravan.state_commands:
        result = caravan.state_commands[command]()
    else:
        print("Wrong command")
    if result == True:
        leave = result
