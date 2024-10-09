

def muestraTablero(A1, A2, A3, A4, A5, A6, A7, A8, A9):
    print(A1, '|', A2, '|', A3)
    print(A4, '|', A5, '|', A6)
    print(A7, '|', A8, '|', A9)

def ingresaJugada(A1, A2, A3, A4, A5, A6, A7, A8, A9):
    print('Ingrese su jugada')
    jugadaValida = False
    while  not jugadaValida:
        mensaje = ''
        fila = int(input('Ingrese una fila (de 1 a 3):'))
        if fila > 3 or fila < 1:
            mensaje = 'La fila ingresada no es válida'
        else:
            columna = int(input('Ingrese una columna (de 1 a 3):'))
            if columna > 3 or columna < 1:
                mensaje = 'La columna ingresada no es válida'
        if mensaje == '':
            fichaColocada = False
            if fila == 1 and columna == 1 and A1 == ' ':
                posicion = 1
                fichaColocada = True
            elif fila == 1 and columna == 2 and A2 == ' ':
                posicion = 2
                fichaColocada = True
            elif fila == 1 and columna == 3 and A3 == ' ':
                posicion = 3
                fichaColocada = True
            elif fila == 2 and columna == 1 and A4 == ' ':
                posicion = 4
                fichaColocada = True
            elif fila == 2 and columna == 2 and A5 == ' ':
                posicion = 5
                fichaColocada = True
            elif fila == 2 and columna == 3 and A6 == ' ':
                posicion = 6
                fichaColocada = True
            elif fila == 3 and columna == 1 and A7 == ' ':
                posicion = 7
                fichaColocada = True
            elif fila == 3 and columna == 2 and A8 == ' ':
                posicion = 8
                fichaColocada = True
            elif fila == 3 and columna == 3 and A9 == ' ':
                posicion = 9
                fichaColocada = True

            if fichaColocada:
                mensaje = 'Su jugada ha sido realizada'
                jugadaValida = True
            else:
                mensaje = 'La casilla elegida está ocupada'
        print(mensaje)
        return posicion

def validaGanador(A1, A2, A3, A4, A5, A6, A7, A8, A9):
    hayUnGanador = False

    # horizontal
    if A1 == A2 == A3 and A1 != ' ':
            hayUnGanador = True
    elif A4 == A5 == A6 and A4 != ' ':
            hayUnGanador = True
    elif A7 == A8 == A9 and A7 != ' ':
            hayUnGanador = True
    # vertical
    elif A1 == A4 == A7 and A1 != ' ':
            hayUnGanador = True
    elif A2 == A5 == A8 and A2 != ' ':
            hayUnGanador = True
    elif A3 == A6 == A9 and A3 != ' ':
            hayUnGanador = True
    # diagonal
    elif A1 == A5 == A9 and A1 != ' ':
            hayUnGanador = True
    elif A3 == A5 == A7 and A3 != ' ':
            hayUnGanador = True

    return hayUnGanador



def jugar():
    A1 = ' '
    A2 = ' '
    A3 = ' '
    A4 = ' '
    A5 = ' '
    A6 = ' '
    A7 = ' '
    A8 = ' '
    A9 = ' '    
    print('Bienvenido al juego del Ta-Te-Ti')
    jugadaNumero = 0
    hayUnGanador = False
    ficha = ['X', 'O']
    while jugadaNumero < 9 and not hayUnGanador:
        muestraTablero(A1, A2, A3, A4, A5, A6, A7, A8, A9)
        posicion = ingresaJugada( A1, A2, A3, A4, A5, A6, A7, A8, A9)
        if posicion == 1:
            A1 = ficha[jugadaNumero % 2]
        elif posicion == 2:
            A2 = ficha[jugadaNumero % 2]
        elif posicion == 3:
            A3 = ficha[jugadaNumero % 2]
        elif posicion == 4:
            A4 = ficha[jugadaNumero % 2]
        elif posicion == 5:
            A5 = ficha[jugadaNumero % 2]
        elif posicion == 6:
            A6 = ficha[jugadaNumero % 2]
        elif posicion == 7:
            A7 = ficha[jugadaNumero % 2]
        elif posicion == 8:
            A8 = ficha[jugadaNumero % 2]
        else:
            A9 = ficha[jugadaNumero % 2]
        jugadaNumero += 1
        if jugadaNumero >= 5:
            hayUnGanador = validaGanador(A1, A2, A3, A4, A5, A6, A7, A8, A9)
            print(hayUnGanador)
            if hayUnGanador:
                print('Felicitaciones ha ganado jugador', (jugadaNumero-1) % 2 +1)
                muestraTablero(A1, A2, A3, A4, A5, A6, A7, A8, A9)
    if not hayUnGanador:
        print('La partida ha finalizado en empate')


