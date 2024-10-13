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

def dibujarOcurrencias(letra, palabra, palabra_secreta):
    nueva_palabra_secreta = []

    for caracter in range(0, len(palabra)):
        # En caso de que la letra no se la indicada y la letra no este codificada dibujar la letra ya existente
        if letra != palabra[caracter] and palabra_secreta[caracter] != "_":
            nueva_palabra_secreta.append(palabra_secreta[caracter])

        # En caso de que la letra sea la correcta dibuja la letra en la ocurrencia
        if letra == palabra[caracter]:
            nueva_palabra_secreta.append(letra)

        # En caso de que la letra no sea la correcta y la letra este codificada entonces dibujar el *
        if letra != palabra[caracter] and palabra_secreta[caracter] == "_":
            nueva_palabra_secreta.append("_")
    
    return "".join(nueva_palabra_secreta)

def juego(palabra_elegida):
    intentos = 6
    caracteres_introduccidos = set()
    caracteres_palabra = set(palabra_elegida)
    palabra_secreta = "_" * len(palabra_elegida)
    adivina = False
    print("La palabra a adivinar es de", (len(palabra_elegida)), "letras")
    
    while intentos >= 0 and not adivina:
        caracter = input("Introduzca una letra: ")

        # Si el caracter ya fue ingresado
        if caracter in caracteres_introduccidos:
            print("Ya has introducido la letra", caracter)
            continue

        # Si el caracter no es correcto se quita un intento y se añade a los caracteres ya ingresados
        if caracter not in caracteres_palabra: 
            intentos -= 1
            caracteres_introduccidos.add(caracter)
            print("Incorrecto - Palabra a adivinar:", palabra_secreta)
        
        # Si el caracter es correcto se reemplaza en todas las ocurrencias y se añade a los caracteres ya ingresados
        if caracter in caracteres_palabra:
            palabra_secreta = dibujarOcurrencias(caracter, palabra_elegida, palabra_secreta)
            caracteres_introduccidos.add(caracter)
            print("Correcto - Palabra a adivinar:", palabra_secreta)
            adivina = "_" not in palabra_secreta

        if intentos == 6:
            dibujar_horca()
        elif intentos == 5:
            dibujarCabeza()
        elif intentos == 4:
            dibujarTorso()
        elif intentos == 3:
            dibujarBrazoIzquierdo()
        elif intentos == 2:
            dibujarBrazoDerecho()
        elif intentos == 1:
            dibujarPiernaIzquierda()
    
    if adivina:
        print("Has adivinado la palabra:", palabra_elegida)
        return 
        
    if intentos <= 0:
        dibujarPiernaDerecha()
        print("Has perdido")
        return 

juego("programacion")