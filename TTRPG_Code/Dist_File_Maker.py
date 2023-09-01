#Dice Distribution
#This code takes a set of dice and calculates all potential results and returns a distribution in array form.

nD = 3 #number of dice
dS = 4 #dice size
mod = 4 #additional modifier

def diceIt(dR, n):
    if dR[n] == dS:
        dR[n] = 1
        dR = diceIt(dR, n+1)
        n -= 1
    else:
        dR[n] += 1
    return(dR)

def diceDist(nD, dS, mod):
    for x in range(nD):
        if x == 0:
            dR = [1]
        else:
            dR.append(1)

    minD = sum(dR)+mod #minimum dice roll
    maxD = (dS*nD)+mod

    dDist = [0] #Initializes array for the probability distribution
    for x in range(maxD-minD):
        dDist.append(0)

    n = 0
    while sum(dR) <= dS*nD:
        dDist[sum(dR)-nD] += 1
        if sum(dR) < dS*nD:
            diceIt(dR, n)
            continue
        else:
            break
    return(dDist)