import Resources.towns_and_roads


# Function(int): Returns(String) name of town by index
def town_by_index(index):
    return Resources.towns_and_roads.towns_names[index]


# Function(String): Returns(int) index of this town in tuple of towns
def get_town_index(town):
    return Resources.towns_and_roads.towns_names.index(town.name)


class Town:
    def __init__(self, name, specialization, richness, size, roads):
        self.name = name
        self.specialization = specialization
        self.richness = richness
        self.size = size
        self.roads = roads

    # (self): Returns(String) specialization of this town
    def get_town_name(self):
        return self.name

    # (self): Returns(specialization_type) specialization of this town
    def get_town_specialization(self):
        return self.specialization

    # (self): Returns(richness_type) richness of this town
    def get_town_richness(self):
        return self.richness

    # (self): Returns(int) size of this town
    def get_town_size(self):
        return self.size

    # Returns(dict String:int) dictionary of towns and distances to them which you can get from here
    def get_connections(self):
        result = {}
        for i in Resources.towns_and_roads.towns_names:
            if self.get_distance_to_town(i) > 0:
                result[i] = self.get_distance_to_town(i)
        return result

    # (self, String): Returns(int) distance from this town to another
    def get_distance_to_town(self, i):
        return Resources.towns_and_roads.roadsMatrix[get_town_index(self.name)][get_town_index(i)]

    # Gives message about town you arrived to
    def arrival(self):
        print("You arrived into town named " + self.name)
# TODO      TradePoint's generation
# TODO      Movement function
