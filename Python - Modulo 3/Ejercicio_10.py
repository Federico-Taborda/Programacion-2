# Si bien esta funcion llega a la solucion no es correcta, ya que se debe
# trabajar solo con numeros
def contar(l:list, palabra:str) -> int:
    if len(palabra) == 0:
        return False
    
    return (palabra[0] == l) + contar(l, palabra[1:])

def contar_for(l:list, cadena:str) -> int:
    contador = 0

    for x in cadena:
        if x == l:
            contador += 1
        
    return contador

def contar_while(l:list, palabra:str) -> int:
    indice = 0
    contador = 0

    while indice < len(palabra):
        if palabra[indice] == l:
            contador += 1
        indice += 1
    
    return contador

def contar_recursiva(l:list, palabra:str, indice:int = 0, contador:int = 0):
    if indice == len(palabra):
        return contador
    
    if palabra[indice] == l:
        return contar_recursiva(l, palabra, indice + 1, contador + 1)
    
    return contar_recursiva(l, palabra, indice + 1, contador)