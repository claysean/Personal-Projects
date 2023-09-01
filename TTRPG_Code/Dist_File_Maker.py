import numpy as np
import pandas as pd

dice = 4
noDice = 3
dieResults = [1]

for x in range(noDice+1):
    dieResults = np.array([dieResults]*5)

print(dieResults)