import pandas as pd
import numpy as np

AttackFile = "C\Users\clays\Documents\GitHub\Personal-Projects\TTRPG_Code\Character Increase Tables\Martial - Attack.csv"
DamageFile = "C:\Users\clays\Documents\GitHub\Personal-Projects\TTRPG_Code\Character Increase Tables\Martial - Damage Spec.csv"
ACFile = "C:\Users\clays\Documents\GitHub\Personal-Projects\TTRPG_Code\Character Increase Tables\Martial - Armor Class.csv"
HPFile = "C:\Users\clays\Documents\GitHub\Personal-Projects\TTRPG_Code\Character Increase Tables\Martial - HP.csv"

#AttackFile = AttackFile.replace("\\", "/")
#DamageFile = DamageFile.replace("\\", "/")
#ACFile = ACFile.replace("\\", "/")
#HPFile = HPFile.replace("\\", "/")

print(AttackFile)

#CharFileList = [AttackFile, DamageFile, ACFile, HPFile]
#CharIncList = []

#for x in CharFileList:
#    CharIncList[x] = pd.read_csv(CharFileList[x])