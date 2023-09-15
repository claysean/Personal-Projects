import DiceDist as dd
import numpy as np
import pandas as pd

csvPath = "C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Damage Distributions - Monster/Damage Increases - "
csvNames = ["Low", "Moderate", "Hard", "Extreme"]
length = len(csvNames)
cNames = ["Level", "nD", "dS", "mod", "Mean", "Min", "Max", "Range", "Std", "-1StD", "+1StD", "-2Std", "+2Std", "Idk", "2Idk"]

for x in range(length):
    mdf = pd.read_csv(csvPath+csvNames[x]+".csv")
    ndf = pd.DataFrame(columns = cNames)
    for c in range(26):
        row = mdf.iloc[c].values.tolist()  
        #1 - Number of Dice, #2 - Size of Dice, #3 - Modifier
        dDist, dResultArr = dd.diceDist(row[1], row[2], row[3])
        dAvg = np.average(dResultArr)
        dMax = np.max(dResultArr)
        dMin = np.min(dResultArr)
        dStd = round(np.std(dResultArr), 2)
        dRange = dMax - dMin
        coverage = round((2*dStd)/dRange, 2)
        coverage2 = round((4*dStd)/dRange, 2)
        m1Std = round(dAvg-dStd, 2)
        p1Std = round(dAvg+dStd, 2)
        m2Std = round(dAvg-(2*dStd), 2)
        p2Std = round(dAvg+(2*dStd), 2)

        mInfo = [c-1, row[1], row[2], row[3], dAvg, dMin, dMax, dRange, dStd, m1Std, p1Std, m2Std, p2Std, coverage, coverage2]
        ndf.loc[c] = mInfo
    name = csvNames[x]+".csv"
    ndf.to_csv(name)