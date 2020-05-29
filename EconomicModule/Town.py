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
        self.name = name
        self.specialization = specialization
        self.richness = richness
        self.size = size
        self.points = []
        for i in range(size):
            randnum = random.randint(1, 6)
            print('\n' + towns_and_roads.point_type[randnum-1] + ':')
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
    def arrival(self):
        print("You arrived into town named " + self.name)

    def print_points(self):
        for i in range(len(self.points)):
            print(self.points[i], '\n')


