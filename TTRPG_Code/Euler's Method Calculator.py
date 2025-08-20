step_size = [.5]
tvals = [1.5, 2]

#number of digits to round to for the step size.
numDigits = [2,2]

t0 = 1
y0 = -1

def equation(t, y, i):
    fn = -1+(2*t)-(4*y)
    yn = y+(fn*step_size[i])
    return yn

n=0

for i in range(len(step_size)):
    yvals = []
    t = t0
    y = y0
    c = 0
    
    while(True):
        
        y = round(equation(t, y, i), 5)
        t = round(t + step_size[i], numDigits[n])
        
        if t == tvals[c]:
            c += 1
            yvals.append(y)
            if c == len(tvals):
                break
    print(tvals)
    print(yvals)
    n += 1


