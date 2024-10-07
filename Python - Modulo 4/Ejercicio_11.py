def conjunto_palbras(texto1:str, texto2:str) -> set:
    return set(texto1.split()) & set(texto2.split())