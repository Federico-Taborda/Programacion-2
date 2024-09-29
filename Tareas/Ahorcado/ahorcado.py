def dibujar_horca():
    return print('''
    _________
   |         |
   |         |
   |         
   |         
   |        
___|___
                 ''')
def dibujarCabeza():
    return print('''
    _________
   |         |
   |         |
   |         0
   |         
   |        
___|___
                 ''')

def dibujarTorso():
    return print('''
    _________
   |         |
   |         |
   |         0     
   |         |
   |        
___|___
                 ''')

def dibujarBrazoIzquierdo():
    return print('''
    _________
   |         |
   |         |
   |         0 
   |        /|
   |         
   |        
___|___
                 ''')

def dibujarBrazoDerecho():
    return print('''
    _________
   |         |
   |         |
   |         0     
   |        /|\`
   |        
___|___
                 ''')

def dibujarPiernaIzquierda():
    return print('''
    _________
   |         |
   |         |
   |         0     
   |        /|\`
   |        /
___|___
                 ''')

def dibujarPiernaDerecha():
    return print('''
    _________
   |         |
   |         |
   |         0  
   |        /|\`
   |        / \`
___|___
                 ''')

def pedirLetra():
    return input("Introduzca una letra: ")

def dibujarOcurrencias(letra, palabra, palabra_secreta):
    nueva_palabra_secreta = ""

    for caracter in range(0, len(palabra)):
        # En caso de que la letra no se la indicada y la letra no este codificada dibujar la letra ya existente
        if letra != palabra[caracter] and palabra_secreta[caracter] != "*":
            nueva_palabra_secreta += palabra_secreta[caracter]

        # En caso de que la letra sea la correcta dibuja la letra en la ocurrencia
        if letra == palabra[caracter]:
            nueva_palabra_secreta += letra

        # En caso de que la letra no sea la correcta y la letra este codificada entonces dibujar el *
        if letra != palabra[caracter] and palabra_secreta[caracter] == "*":
            nueva_palabra_secreta += "*" 
    
    return nueva_palabra_secreta

def adivinaPalabra(palabra_secreta):
    return "*" not in palabra_secreta

def juego(palabra_elegida):
    intentos = 6
    caracteres_introduccidos = []
    palabra = palabra_elegida
    palabra_secreta = "*" * len(palabra)
    adivina = False
    print("La palabra a adivinar es de", (len(palabra)), "letras")
    dibujar_horca()
    
    while intentos >= 0 and not adivina:
        caracter = pedirLetra()

        if caracter in caracteres_introduccidos:
            intentos -= 1
            print("Ya has introducido la letra", caracter)

        if caracter not in palabra:
            intentos -= 1
            caracteres_introduccidos.append(caracter)
            print("Incorrecto - Palabra a adivinar:", palabra_secreta)
        
        if caracter in palabra:
            palabra_secreta = dibujarOcurrencias(caracter, palabra, palabra_secreta)
            caracteres_introduccidos.append(caracter)
            print("Correcto - Palabra a adivinar:", palabra_secreta)
            adivina = adivinaPalabra(palabra_secreta)

        if intentos == 5:
            dibujarCabeza()
        if intentos == 4:
            dibujarTorso()
        elif intentos == 3:
            dibujarBrazoIzquierdo()
        elif intentos == 2:
            dibujarBrazoDerecho()
        elif intentos == 1:
            dibujarPiernaIzquierda()
    
    if adivina:
        print("Has adivinado la plabra:", palabra)
        return 
        
    if intentos <= 0:
        dibujarPiernaDerecha()
        print("Has perdido")
        return 

juego("programacion")