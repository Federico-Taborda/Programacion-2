# Juego de la memoria
# El juego consiste en repetir las misma secuencia de letras en el mismo orden que el jugador anterior
# El primer jugador en fallar la secuencia pierde

# Ingresar nombres e indicar quien juega primero
def ingresar_datos():
    primer_jugador = input("Ingresar nombre del primer jugador: ")
    segundo_jugador = input("Ingresar nombre del segundo jugador: ")
    quien_juega = input("Ingrese el nombre de quien es turno: ")
    
    jugador_uno = { "nombre": primer_jugador, "turno": False }
    jugador_dos = { "nombre": segundo_jugador, "turno": False }
    
    if quien_juega == jugador_uno["nombre"]:
        return ( jugador_uno, jugador_dos )
    elif quien_juega == jugador_dos["nombre"]:
        return ( jugador_dos, jugador_uno )
    else:
        quien_juega = input("Ingrese el nombre de quien es turno: ")
    
# Inicio del juego
def jugar():
    jugador_actual, jugador_anterior = ingresar_datos()
    turno_actual = []
    turno_anterior = []
    juego_termina = False
    indice = 0
    
    while not juego_termina:
        print(f"Juega {jugador_actual['nombre']}")
        letra = input("Ingrese una letra: ")
        
        # Verifica que el caracter ingresado sea correcto
        if not letra.isalpha() or len(letra) > 1:
            continue
        
        turno_actual.append(letra)
        
        # Logica de cambiar turno
        if len(turno_anterior) < len(turno_actual):
            turno_anterior = turno_actual
            turno_actual = []
            aux = jugador_actual
            jugador_actual = jugador_anterior
            jugador_anterior = aux
            indice = 0
            continue
        
        # Compara la letra actual con la letra del mismo indice del turno anterior
        if turno_actual[indice] == turno_anterior[indice]:
            pass
        else:
            juego_termina = True
            print("Gana", jugador_anterior["nombre"])
            break
            
        indice += 1

jugar()