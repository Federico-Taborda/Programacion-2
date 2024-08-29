def promediar_notas(notas):
    promedio = 0
    for nota in notas:
        promedio += nota

    return print(promedio / len(notas))


def ingresar_notas():
    notas = []
    continuar = False

    while not continuar:
        nota = input("Ingrese una nota o end para finalizar:")

        if nota == "end":
            continuar = True
            return promediar_notas(notas)

        notas.append(int(nota))

ingresar_notas()