def busqueda_binaria(lista:list, elemento:any) -> int:
    primero = 0
    ultimo = len(lista) - 1
    mitad = len(lista) // 2
    encontrado = False
    index = 0
    
    while not encontrado:
        if lista[primero] == elemento:
            encontrado = True
            index = primero
        
        if lista[ultimo] == elemento:
            encontrado = True
            index = ultimo
        
        if lista[mitad] == elemento:
            encontrado = True
            index = mitad
            
        if lista[mitad] > elemento:
            ultimo = mitad
            mitad = ultimo // 2
        
        if lista[mitad] < elemento:
            primero = mitad + 1
            mitad = mitad + (ultimo - mitad) // 2

        if lista[mitad] != elemento:
            print(lista[:mitad])
            encontrado = True

    return index


    