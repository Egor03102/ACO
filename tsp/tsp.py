import numpy as np

from ants import Colony
from cnf import ITERATIONS

class Tsp:
    def __init__(self, count, roads):
        # count is the quantity of points
        # roads it's the list in the following template [(point1, point2, distance),]
        # points should be integer and from 0 to count - 1

        self.count = count
        self.roads_list = roads
        self.roads = self.generate_array_roads() # roads array
        self.cities = {} # key is name of city and value is visited or not (0 or 1)
        self.add_cities(self.count)
    
    def generate_array_roads(self):
        roads_array = np.zeros((self.count, self.count), dtype=int)
        for x, y , weight in self.roads_list:
            roads_array[x][y] = roads_array[y][x] = weight # fill two values xy and yx
        return roads_array
    
    def add_cities(self, n):
        for i in range(n):
            self.cities[i] = 0
    
    def solve_aco(self):
        colony = Colony(self.count)
        for _ in range(ITERATIONS):
            colony.move_colony(self.cities, self.roads)
        return colony.get_best_distance(), colony.get_best_path() # distance and path in tuple









