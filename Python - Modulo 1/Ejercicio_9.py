# Dados dos numeros (a, b) la funcion devolvera la suma de los mismos
def suma(a:int, b:int) -> int:
    return a + b

# Dados dos numeros (a, b) la funcion devolvera la resta de los mismos
def resta(a:int, b:int) -> int:
    return a - b

# Dados dos numeros (a, b) la funcion devolvera la multiplicacion de los mismos
def multiplicacion(a:int, b:int) -> int:
    return a * b

# Dados dos numeros (a, b) la funcion devolvera la division de los mismos
def division(a:int, b:int) -> int:
    if(b == 0):
        return "No se puede dividir por cero"
    
    return a / b

def introducir_valores(operar):
    a = int(input("Primer valor: "))
    b = int(input("Segundo valor: "))

    print(operar(a, b))

    return calculadora()

def calculadora():
    print("""
          1. Suma
          2.Resta
          3.Multiplicacion
          4.Divide
          5.Salir""")
    
    opcion = int(input("Elija una operacion"))

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
        return calculadora()

#calculadora()