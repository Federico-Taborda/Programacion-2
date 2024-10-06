def diaSiguiente(fecha:tuple) -> tuple:
    if fecha[0] == 30 and fecha[1] == 12:
        return (1, 1, fecha[2] + 1)
    
    if fecha[0] == 30:
        return (1, fecha[1] + 1, fecha[2])
    
    return (fecha[0] + 1, fecha[1], fecha[2])

print(diaSiguiente((30, 12, 2000)))