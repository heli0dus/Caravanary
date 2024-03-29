import Resources.towns_and_roads as towns_and_roads
import EconomicModule.TradePoint as TradePoint
import random as random


# Function(int): Returns(String) name of town by index
def town_by_index(index):
    return towns_and_roads.towns_names[index]


# Function(String): Returns(int) index of this town in tuple of towns
def get_town_index(town):
    return towns_and_roads.towns_names.index(town.name)


class Town:
    def __init__(self, name, specialization, richness, size):
        self.name = name                        # town name
        self.specialization = specialization    # town specialization
        self.richness = richness                # town richness
        self.size = size                        # town size
        self.points = []                        # list of town TradePoint's
        for i in range(size):
            randnum = random.randint(1, 5)
            a = TradePoint.TradePoint(self, towns_and_roads.point_type[randnum-1])
            self.points.append(a)

    def arrival(self):
        print("You arrived into town named " + self.name)

    def print_points(self):
        for i in range(len(self.points)):
            print(self.points[i], '\n')

    def re_generate_points(self):
        self.points.clear()
        for i in range(self.size):
            randnum = random.randint(1, 5)
            a = TradePoint.TradePoint(self, towns_and_roads.point_type[randnum-1])
            self.points.append(a)

    # # Returns(dict String:int) dictionary of towns and distances to them which you can get from here
    # def get_connections(self):
    #     result = {}
    #     for i in towns_and_roads.towns_names:
    #         if self.get_distance_to_town(i) > 0:
    #             result[i] = self.get_distance_to_town(i)
    #     return result

    # # (self, String): Returns(int) distance from this town to another
    # def get_distance_to_town(self, i):
    #     return towns_and_roads.roadsMatrix[get_town_index(self.name)][get_town_index(i)]

    # Gives message about town you arrived to

real_towns_names = {
    "Aibiusa": Town("Aibiusa", "farm", "poor", 2),
    "Zebrige": Town("Zebrige", "capital", "capital", 12),
    "Anosi": Town("Anosi", "forgery", "rich", 6),
    "Vleles": Town("Vleles", "port", "poor", 3),
    "Brario": Town("Brario", "farm", "normal", 5),
    "Strover": Town("Strover", "forgery", "normal", 3),
    "Beksburg": Town("Beksburg", "port", "rich", 8),
    "Zheocester": Town("Zheocester", "farm", "poor", 1),
}

