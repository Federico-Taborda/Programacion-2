# Solucion utilizando recursion
def solicitar_contraseña(intentos):
    contraseña_guardada = "admin"

    if intentos == 0:
        return print("Maximo de intentos excedido")

    contraseña_ingresada = input("Ingrese su contraseña: ")

    while not contraseña_ingresada == contraseña_guardada:
        print("Contraseña incorrecta. Vuelva a intentarlo")
        return solicitar_contraseña(intentos - 1)
    
    return print("Contraseña correcta")

#solicitar_contraseña(5)

# Solucion utilizando iteracion
def solicitar_contraseña():
    contraseña_inventada = "admin"
    intentos = 0
    cantidad_maxima_intentos = 3
    coincide = False

    while intentos < cantidad_maxima_intentos and not coincide:
        contraseña_ingresada = input("Ingrese una contraseña: ")
        
        if contraseña_ingresada == contraseña_inventada:
            coincide = True
        else:
            intentos += 1

    return coincide

#print(solicitar_contraseña())
