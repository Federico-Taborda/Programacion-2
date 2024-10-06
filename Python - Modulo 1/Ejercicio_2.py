def primeros_veinticinco_naturales(contador = 0, m = 0):
    if contador == 100:
        return 
    
    if m % 2 == 0:
        print(m)
        return primeros_veinticinco_naturales(contador + 1, m + 1)
    
    return primeros_veinticinco_naturales(contador, m + 1)

print(primeros_veinticinco_naturales())