notas = {
    "Federico": [1, 1, 6],
    "Gabriel": [7, 7, 8],
    "Ezequiel": [8, 9, 8]
}

def promedio(notas:list) -> dict:
    diccionario = {}

    for alumno in notas:
        total = 0
        for nota in notas[alumno]:
            total += nota
        
        diccionario[alumno] = total // len(notas[alumno])

    return diccionario

#print(promedio(notas))



