import pandas as pd

AttackFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Attack.csv'
DamageFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Damage Spec.csv'
ACFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - Armor Class.csv'
HPFile = 'C:/Users/clays/Documents/GitHub/Personal-Projects/TTRPG_Code/Character Increase Tables/Martial - HP.csv'

attackdf = pd.read_csv(AttackFile)
damagedf = pd.read_csv(DamageFile)
ACdf = pd.read_csv(ACFile)
HPdf = pd.read_csv(HPFile)

df = pd.concat([attackdf[cl], damagedf[cl], ACdf[cl], HPdf[cl]], axis=1)

print(df)