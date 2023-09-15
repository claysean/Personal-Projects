#Dice Distribution
#This code takes a set of dice and calculates all potential results and returns a distribution in array form.

#number of dice = nD
#dice size = dS
#additional modifier = mod

def diceIt(dR, dS, n):
    if dR[n] == dS:
        dR[n] = 1
        dR = diceIt(dR, dS, n+1)
        n -= 1
    else:
        dR[n] += 1
    return(dR)

#Takes number of dice, dice size and modifier and creates a distribution.
def diceDist(nD, dS, mod):
    for x in range(nD):
        if x == 0:
            dR = [1]
        else:
            dR.append(1)

    minD = sum(dR)+mod #minimum dice roll
    maxD = (dS*nD)+mod #maximum dice roll

    dDist = [0] #Initializes array for the probability distribution
    for x in range(maxD-minD):
        dDist.append(0)

    n = 0
    b = 1
    dResultArr = []

    while sum(dR) <= dS*nD:
        dDist[sum(dR)-nD] += 1
        dResultArr.append(sum(dR)+mod)
        if sum(dR) < dS*nD:
            diceIt(dR, dS, n)
            continue
        else:
            break
    return(dDist, dResultArr)