# Practica 5 - Ejercicio 5

# Convierte caracteres (en minuscula) a caracteres cifrados (en minuscula)
def encriptar_caracter(c):
    
    # No consideramos la ñ por simplicidad.
    long_alfabeto = 26
    indice_alfabeto = ord(c) - ord("a")
    indice_cifrado = (indice_alfabeto + 13) % long_alfabeto
    caracter_cifrado = chr(indice_cifrado + ord("a"))
    return caracter_cifrado


def encriptar_linea(linea: str) -> str:
    chars_encriptados = []
    
    for c in linea:
        if c.isalpha():
            mayus = c.isupper()
            cifrado = encriptar_caracter(c.lower())

            if mayus:
                cifrado = cifrado.upper()
            
            chars_encriptados.append(cifrado)
        
        else:
            chars_encriptados.append(c)
    
    return "".join(chars_encriptados)


def encriptar_archivo(origen : str, destino: str):

    archivoOrigen  = open(origen, "r")
    archivoDestino = open(destino, "w")

    for linea in archivoOrigen:
        archivoDestino.write(encriptar_linea(linea))

    archivoOrigen.close()
    archivoDestino.close()


def encriptar_archivo_with(origen : str, destino: str):

    with open(origen, "r") as archivoOrigen:
        with open(destino, "w") as archivoDestino:

            for linea in archivoOrigen:
                archivoDestino.write(encriptar_linea(linea))


def main():

    encriptar_archivo("origen.txt", "destino.txt")
    # encriptar_archivo_with("origen.txt", "destino.txt")


if __name__ == "__main__":
    main()

