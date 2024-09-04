def lucas(a,b,i):
    if i == 1:
        return b
    
    return lucas(b, a + b, i - 1)

def lucas_for(a,b,i):
    for i in range(i):
        c = a + b
        a = b
        b = c
    return a 

def lucas_while(a, b, i):
    l = [a,b]
    
    while i >= len(l):
        l.append (l[-1] + l[-2])

    return l[-1]