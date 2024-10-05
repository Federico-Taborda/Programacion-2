def conjunto_palbras(texto1:str, texto2:str) -> set:
    lista = texto1.split() + texto2.split()
    return set(lista)

print(conjunto_palbras("esto es una cadena", "esto es otra cadena"))