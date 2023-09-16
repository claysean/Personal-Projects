import pandas as pd

AttackFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Attack.csv'
DamageFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Damage Spec.csv'
ACFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Armor Class.csv'
HPFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - HP.csv'

files = [AttackFile, DamageFile, ACFile, HPFile]
columnNames = ["Attack", "Damage", "AC", "HP"]
for x in range(len(files)):
    stringToChange = files[x]
    files[x] = stringToChange.replace("clays", "sean")

attackdf = pd.read_csv(files[0])
damagedf = pd.read_csv(files[1])
ACdf = pd.read_csv(files[2])
HPdf = pd.read_csv(files[3])
classes = list(attackdf.columns.values)
classes.remove('Level')

for x in classes:
    classdf = pd.DataFrame([attackdf[x],damagedf[x],ACdf[x],HPdf[x]], columnNames)
    classdf = classdf.transpose()
    for c in range(3):
        for b in range(20):
            if b == 0:
                classdf.iat[b,c] = classdf.iat[b,c]+1
            else:
                classdf.iat[b,c] = classdf.iat[b,c]+classdf.iat[b-1,c]+1
    classdf.to_csv("Character Increase Tables/" + x + ".csv")