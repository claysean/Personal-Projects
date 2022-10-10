#Random Creature Generator

import numpy as np
from numpy import random
import pandas as pd

numMonsters = 6 #how many monsters to generate?
c = 0 #don't touch

file_name = 'C:/Users/Owner/OneDrive/Documents/Freak of the Week(1).xlsx'

#takes the front Freak of the week sheet and turns into dataframe
datatypes = pd.read_excel(file_name, sheet_name = "Data", index_col=0)
sheet_names = list(datatypes.columns.values)
noColumns = len(sheet_names)

#makes an array to store the characteristics based off of number of monsters
charac_list = []
for x in range(numMonsters):
    charac_list.append(0)

#takes random string per category in a sheet and adds them to a monster profile
for x in range(len(sheet_names)):
    currData = pd.read_excel(file_name, sheet_name = sheet_names[x], index_col=0)
    currColumns = list(currData.columns.values)
    numOptsInColumns = currData.count(axis=0)
    
    for a in range(len(currColumns)): #a is the current column selected
        
        col_opts = numOptsInColumns.iat[a]
        
        for b in range(numMonsters):
            rand_val = random.randint(col_opts) #generates a random value based off of number of options in column
            charac_list[b] = currData.iat[rand_val, a]
        charS = pd.Series(data = charac_list, name = currColumns[a])
       
        if a == 0 and c == 0:
            charFrame = pd.DataFrame(data = charS)
            c = 1
        else:
            charFrame.insert(loc = c, column = currColumns[a], value = charS)
            c += 1

charFrame.to_csv('Freak of the Week.csv')