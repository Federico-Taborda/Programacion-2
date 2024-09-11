def promediar_notas(notas):
    promedio = 0
    for nota in notas:
        promedio += nota

    return print(promedio / len(notas))

def ingresar_notas():
    notas = []
    continuar = True

    while continuar:
        nota = input("Ingrese una nota o end para finalizar:")

        if nota == "end":
            continuar = False

        notas.append(int(nota))

    return promediar_notas(notas)

#ingresar_notas()

def ingresar_notas_dos():
    suma_notas = 0
    cantidad_notas = 0
    seguir = True 

    while seguir:
        nota = float(input("Ingresar una nota: "))
        suma_notas += nota
        cantidad_notas += 1

        continuar = (input("Desea salir?: "))

        if not "s" == continuar:
            seguir = False

    return suma_notas / cantidad_notas

#print("El promedio es: ", ingresar_notas_dos())