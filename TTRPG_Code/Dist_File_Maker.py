dS = 4 #dice size
nD = 2 #number of dice

def diceIt(dR, n):
    if dR[n] == 

for x in range(nD):
    if x == 0:
        dR = [1]
    else:
        dR.append(1)

m = sum(dR) #minimum dice roll
dDist = []
n = 0

while sum(dR) <= dS*nD:
    dDist[sum(dR)-nD] += 1
    if sum(dR) < dS*nD:
        continue
    else:
        break

print(dR)