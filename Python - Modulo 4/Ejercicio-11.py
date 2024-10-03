def conjunto_palbras(texto1, texto2):
    lista = texto1.split() + texto2.split()
    return set(lista)

#print(conjunto_palbras("esto es una cadena", "esto es otra cadena"))