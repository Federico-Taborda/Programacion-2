def contar_palabras_for(cadena):
    palabra = ""
    contador = 0

    for x in range(0, len(cadena)):
        if cadena[x] != " ":
            palabra += cadena[x]

        else:
            if len(palabra) > 5:
                contador += 1 
            palabra = ""

    return contador

def test_contar_palabras():
    assert contar_palabras_for("tengo guardado mucho dinero en mi casa") == 2
    assert contar_palabras_for("hola mundo") == 0
    #assert contar_palabras_for("letras") == 1
