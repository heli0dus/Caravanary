import Resouces.towns_and_roads


# Function(int): Returns(String) name of town by index
def town_by_index(index):
    return Resouces.towns_and_roads.towns_tuple[index]


# Function(String): Returns(int) index of this town in tuple of towns
def get_town_index(town):
    return Resouces.towns_and_roads.towns_tuple.index(town.name)


class Town:
    def __init__(self, name, specialization, richness, size, roads):
        self.name = name
        self.specialization = specialization
        self.richness = richness
        self.size = size
        self.roads = roads

    # (self, String): Returns(int) distance from this town to another
    def get_distance_to_town(self, i):
        return Resouces.towns_and_roads.roadsMatrix[get_town_index(self.name)][get_town_index(i)]

    # Returns(dict String:int) dictionary of towns and distances to them which you can get from here
    def get_connections(self):
        result = {}
        for i in Resouces.towns_and_roads.towns_tuple:
            if self.get_distance_to_town(i) > 0:
                result[i] = self.get_distance_to_town(i)
        return result

    # Gives message about town you arrived to
    def arrival(self):
        print("You arrived into town named " + self.name)
