# Ejercicio A
def promedio(notas:list) -> dict:
    diccionario = {}

    for alumno in notas:
        total = 0
        for nota in notas[alumno]:
            total += nota
        
        diccionario[alumno] = total // len(notas[alumno])

    return diccionario

# Ejercicio B
def mayor_promedio(notas:list) -> str:
    promedios = promedio(notas)

    mayor_promedio = 0
    mejor_alumno = ""

    for alumno in promedios:
        if promedios[alumno] > mayor_promedio:
            mejor_alumno = alumno
    
    return mejor_alumno

