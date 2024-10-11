def suma(a:int, b:int) -> int:
    return a + b

def resta(a:int, b:int) -> int:
    return a - b

def multiplicacion(a:int, b:int) -> int:
    return a * b

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

    # Uso de funciones de alto orden. Se pasa la operacion necesitada dependiendo del valor introducido
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