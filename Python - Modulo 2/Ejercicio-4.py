# factorial :: Number -> Number
# Dado un numero n la funcion devolvera el factorial de n
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6

def mostrar_factorial():
    numero = input("Ingrese un numero: ")

    if not numero.isnumeric():
        print("Solo se puede ingresar numeros")
        return mostrar_factorial()

    print(factorial(int(numero)))
    return mostrar_factorial()

mostrar_factorial()
