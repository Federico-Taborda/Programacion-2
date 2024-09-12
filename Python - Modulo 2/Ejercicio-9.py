def preguntar():
    n = input("Ingresar primer numero: ")
    m = input("Ingresar segundo numero: ")

    if n[0].isnumeric() or n[1].isnumeric() and m[0].isnumeric() or m[1].isnumeric():
        while not int(n) < int(m):
            m = input("Ingresar segundo numero:")
    else:
        print("Valores incorrectos")
        preguntar()

    return print(n, m)

preguntar()

