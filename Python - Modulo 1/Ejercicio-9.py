# suma :: Number Number -> Number
# Dados dos numeros (a, b) la funcion devolvera la suma de los mismos
def suma(a, b):
    return a + b

# resta :: Number Number -> Number
# Dados dos numeros (a, b) la funcion devolvera la resta de los mismos
def resta(a, b):
    return a - b

# multiplicacion :: Number Number -> Number
# Dados dos numeros (a, b) la funcion devolvera la multiplicacion de los mismos
def multiplicacion(a, b):
    return a * b

# division :: Number Number -> Number
# Dados dos numeros (a, b) la funcion devolvera la division de los mismos
def division(a, b):
    if(b == 0):
        return "No se puede dividir por cero"
    
    return a / b

def introducir_valores(operar):
    a = int(input("Primer valor: "))
    b = int(input("Segundo valor: "))

    print(operar(a, b))

    return operacion()

def operacion():
    print("1. Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Divide")
    print("5.Salir")
    opcion = int(input("Ingrese un numero: "))

    if opcion == 1: 
        introducir_valores(suma)
    elif opcion == 2:
        introducir_valores(resta)
    elif opcion == 3:
        introducir_valores(multiplicacion)
    elif opcion == 4:
        introducir_valores(division)
    elif opcion == 5:
        print("Ha salido del programa")
    else:
        print("Tecla presionada incorrecta")
        return operacion()

operacion()