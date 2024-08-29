contraseña_guardada = "admin"

def validar_contraseña(contraseña):
    return contraseña == contraseña_guardada

def solicitar_contraseña(intentos):
    if intentos == 0:
        return print("Maximo de intentos excedido")

    contraseña = input("Ingrese su contraseña: ")

    while not validar_contraseña(contraseña):
        print("Contraseña incorrecta. Vuelva a intentarlo")
        return solicitar_contraseña(intentos - 1)
    
    return print("Contraseña correcta")

solicitar_contraseña(5)
