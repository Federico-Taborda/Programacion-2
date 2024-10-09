# Representamos palabras con listas de caracteres.

def apariciones(ls,e): 
    "Esta función auxiliar calcula la cantidad de veces que aparece un elemento en una lista."
    contador = 0
    for elem in ls:
        if elem == e:
            contador += 1
    return contador

def listaCad(ls):
    "Función auxiliar, dada una lista. Devuelve la lista en forma de cadena, el primer elemento es la primer letra y así."
    cadena = ""
    for i in ls:
        cadena += i
    return cadena

def IngresarPalabra(): # Pide ingresar una palabra al usuario.
    "Sistema de ingreso de palabra, Devuelve la palabra en forma de lista de carácteres lowercase."
    palabra = str(input("Ingrese la palabra a adivinar:")).lower()
    return list(palabra) # Devuelve la misma en forma de lista, donde sus elementos son los caracteres correspondientes.

def Intentos(ls): 
    "Función auxiliar, dado una lista compara su logitud con 6. Devuelve un booleano"
    return len(ls) == 6

def Comparar(ls1,ls2):
    "Función auxiliar, dadas dos listas compara sus longitudes. Devuelve un booleano."
    return len(ls1) == len(ls2)

def MensajeIntentos(ls):
    "Función auxiliar, dada una lista imprime el resultado de la diferencia entre 6 y la longitud de la lista. Devuelve un número."
    print("Esa letra no está en la palabra, te quedan",(6 - len(ls)),"Intentos")
    

def ImprimirPalabra(palabra):
    "Muestra la palabra como el juego del ahorcado, por cada letra que todavía no se encontró muestra un guión y así..."
    # Mostrar la palabra con las letras adivinadas y espacios en blanco
    MostrarPalabra = ' '.join(['_' if char == '_' else char for char in palabra])
    print("Palabra a adivinar: ", MostrarPalabra)
    


def main():
    "Código main del juego."
    
    lista_Estan = [] # Lista letras ingresadas que están en la palabra.
    lista_NoEstan = [] # Lista de letras ingresadas que NO están en la palabra.
    mensaje = ""
    
    lista_Palabras = IngresarPalabra() # Pide al usuario ingresar una palabra a adivinar.
    palabra_oculta = ['_' for _ in lista_Palabras] # Lista que muestra el estado actual de la palabra.
    
    while (not Comparar(lista_Palabras,lista_Estan)) and (not (Intentos(lista_NoEstan))): # Condiciones para terminar el juego.
        
        letra = str(input("Ingrese una letra:")) # Pide al jugador ingresar letras.
        
        if (letra in lista_Palabras) and (not letra in lista_Estan): # Caso de la letra ingresada está en la palabra.
            lista_Estan.extend([letra] * apariciones(lista_Palabras, letra)) # Agrega la letra tantas veces aparece en la palabra a adivinar.
            
            for i, c in enumerate(lista_Palabras):
                if c == letra:
                    palabra_oculta[i] = letra
            
        else:
            if (not letra in lista_NoEstan) and (not letra in lista_Estan):
                lista_NoEstan.append(letra) # Caso de la letra ingresada NO está en la palabra.
                MensajeIntentos(lista_NoEstan)
            elif (letra in lista_NoEstan): 
                print("Ya intentaste con esa letra.")
                print("Letras ya intentadas que no están en la palabra:",lista_NoEstan) # Imprime la lista de letras que NO están en la palabra.
            else: # Si la letra ingresada ya fué ingresada anteriormente y está en la palabra a adivinar.
                print("Esa letra ya está en la palabra.")

        ImprimirPalabra(palabra_oculta) # Mostrar el estado de la palabra.
        
    if Comparar(lista_Palabras,lista_Estan): # Caso ganaste.
        mensaje = "¡Ganaste el juego!"
                
    elif Intentos(lista_NoEstan): # Caso te quedaste sin intentos.
        mensaje = "Te quedaste sin intentos. La palabra era " + listaCad(lista_Palabras)
        
    
    print(mensaje)

if __name__ == "__main__":
    main()


