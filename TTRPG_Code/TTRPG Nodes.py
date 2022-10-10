#Distance between planets is lightyears away from one another
#Goal is to randomly drop planets in a way that makes sense and to be able to see them graphically

import numpy as np
import matplotlib.pyplot as plt
from numpy import random
import pandas as pd
import time

planets = ["Earth","Mars","Jupiter","Saturn","Uranus","Mercury","Neptune"]
axes = ['x','y','z']
planSpaceMax = [2000, 2000, 2000] #Maximum x, y, z boundaries
minimumPlanDist = 1 #Minimum number of lightyears away

coord = []
for x in range(len(planets)):
    coord.append(0)

#generate coordinates
def planetCoordGen():
    for a in range(len(axes)):
        for b in range(len(planets)):
            coord[b] = random.randint(planSpaceMax[a])/100
        planetsList.insert(a+1, axes[a], coord)
    
#check distance

planetsList = pd.DataFrame(data = planets, columns = ["Planets"])
planetCoordGen()
print(planetsList)