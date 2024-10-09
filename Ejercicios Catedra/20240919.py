from random import randint

def eliminaDuplicados(l):
    rl = []
    for i in l:
        if i not in rl:
            rl.append(i)
    return rl

def eliminaDuplicados2(l):
    if l == []:
        return l
    l.sort()
    rl = [l[0]]
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            rl.append(l[i])
    return rl
    
def f(n = 100000):
    l1 = list(range(n)) 
    l2 = list(range(n))
    l2.reverse()
    return l1 + l2        

def lista(n=100000):
    ls = [randint(-1000000, 1000000) for _ in range(n)]
    ls.sort()
    return ls

def dicotomica_R (l, e):
    if l == []:
        return False
    m = len(l)//2
    if (e > l[m]):
        return dicotomica_R(l[m+1:],e)
    elif (e < l[m]):
        return dicotomica_R(l[:m],e)
    else:
        return True

def dicotomica_I (l, e):
    m = len(l) // 2
    while (l != [] and l[m] != e):
        if (e < l[m]):
            l = l[:m]
        else: 
            l = l[m+1:]
        m = len(l) // 2
    return l != []

def dicotomica_R2 (l, e, i, f):
    if i == f:
        return False 
    m = (i + f) // 2
    if (e > l[m]):
        return dicotomica_R2(l,e,m+1,f) 
    elif (e < l[m]):
        return dicotomica_R2(l,e,i,m)
    else:
        return True
    
def dicotomica_I2 (l, e):
    i = 0
    f = len(l)
    m = (i + f) // 2
    while (i != f and l[m] != e):
        if (e > l[m]):
            i = m+1
        else:
            f = m
        m = (i + f) // 2
    return l[m] == e

def busqueda (l, e):
    for elem in l:
        if elem == e:
            return True 
    return False

def buscar_todos (l):
    for i in range(100000):
        busqueda(l, i)

def buscar_todos_D (l):
    l.sort()
    for i in range(100000):
        dicotomica_I2(l, i)