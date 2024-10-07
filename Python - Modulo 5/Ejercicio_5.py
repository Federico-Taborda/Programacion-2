def rot13(archivo_origen, archivo_destino):
    file = open(archivo_origen, "r")

    for linea in file:
        linea_cifrada = cifrar_linea(linea)
        guardar_linea_cifrada(linea_cifrada, archivo_destino)
    
    file.close

def cifrar_linea(linea):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    linea_cifrada = ""

    for caracter in range(0, len(linea)):
        if linea[caracter] != " " and linea[caracter] != "\n" :        
            indice = alfabeto.index(linea[caracter].lower())

            if indice + 13 > (len(alfabeto) - 1):
                indice = (indice + 13) - len(alfabeto)
            else:
                indice += 13
            
            linea_cifrada += alfabeto[indice]
        
        if linea[caracter] == " ":
            linea_cifrada += " "

    return linea_cifrada + "\n"

def guardar_linea_cifrada(linea, archivo):
    file = open(archivo, "a")
    file.write(linea)
    file.close

def main():
  rot13("oraciones.txt", "oraciones-cifradas.txt")
  rot13("oraciones-cifradas.txt", "oraciones-desifradas.txt")
  
if __name__ == "__main__":
  main()