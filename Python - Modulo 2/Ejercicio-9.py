def ingresar_numero(texto):
    dato = int(input(texto))
    return dato

def preguntar():
    n = ingresar_numero("Ingresar primer numero: ")
    m = ingresar_numero("Ingresar segundo numero:")

    while not n < m:
        m = ingresar_numero("Ingresar segundo numero:")

    return print(n, m)

preguntar()

