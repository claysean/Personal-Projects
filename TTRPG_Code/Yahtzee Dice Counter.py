import pandas

def diceIterator(diceResults, n, arrSize):
    n = n + 1
    if n >= arrSize:
        return diceResults, n
    elif diceResults[n] == 6:
       diceResults[n] = 1
       diceResults, n = diceIterator(diceResults, n, arrSize)
    else:
       diceResults[n] = diceResults[n] + 1
       n = n - 1
       return diceResults, n
    n = n - 1
    return diceResults, n

def yahtzee(diceResults, arrSize):
    i = 1
    for x in diceResults:
       if diceResults[0] == diceResults[i]:
          i = i + 1
          if i == arrSize:
             print(diceResults)
             return True
          continue
       else:
          return False

diceResults = [1,1,1,1,1]
n = 0
arrSize = 5
i = 0
yahtzees = 0
fourkinds = 0
threekinds = 0

for x in range(7776):
   if(yahtzee(diceResults, arrSize)):
      yahtzees = yahtzees + 1
      fourkinds = fourkinds + 1
      threekinds = threekinds + 1
   i = i + 1
   if diceResults[0] == 6:
      diceResults[0] = 1
      diceResults, n = diceIterator(diceResults, n, arrSize)
   else:
      diceResults[0] = diceResults[0]+1
      
print(yahtzees)