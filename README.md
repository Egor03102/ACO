# ACO
Finding the optimal route through all points. <br>
Class Tsp (tsp.py) accepts two parameters: the number of points and a list of roads in the format [(1, 2, distance), (2, 3, distance), etc.].
Method solve_aco returns the best distance and path
ants.py contains the algorithm
# Working algorithm
The algorithm works in following steps:
1. Initialization a colony of ants
2. Move colony a few times
3. Every ant go whole path
4. Update pheromones
5. Stopping the algorithm when the best solution stagnates
6. Choose the best ant
## Moving colony
When you move colony one time, the every ant go through all points.
How to an ant choosing the next road. There is a formula for calculating
The decision to visit the next point is influenced by two coefficients: alpha, which increases the strength of pheromones, and beta, which affects the distance to the point.
$\frac{(pheromones \ on \ specific path)^a * (1 \ / \  distance \ on \ specific \ path)^b}{((sum \ of \  pheromones \ on \ path)^a * (1 \ / \ sum \ of \ distances)^b)}$
## Update pheromones
To update the pheromones, add k = 1 / distance to road traveled
## cnf
In config, there are some options that necessary for algorithm
1. Alpha
2. Beta
3. EVAPORATION
   How long or how fast will the pheromones evaporate
4. ANTS_FACTOR
   Еhe number of ants, depending on the number of points
5. ITERATIONS
  How many times colony will be moved

# Usage Example
```python
from random import randint

from tsp import Tsp

# usage example for symmetric roads

# variable for roads
roads = []

# number of points 
n = 10

# creating the roads [(first, second, distance), ()]
for first in range(n + 1):
    for second in range(first + 1, n):
        roads.append((first, second, randint(1, 1000))) # random distance

# create new variable with object class Tsp
tsp = Tsp(n, roads)

# use solve_aco() that returns the optimal distance and path
distance, path = tsp.solve_aco()

print(distance, path)
```
