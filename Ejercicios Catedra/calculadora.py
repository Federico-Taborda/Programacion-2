def menuPrincipal():

    print("------------------")

    print("1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n5. Salir")

    opcion = int(input("\nIngrese una opcion: "))

    # Si la opcion ingresada esta asociada a una operacion artimética
    # ingreso los argumentos correspondientes.

    if 1 <= opcion and opcion <= 4: # Equivalente a: 1 <= opcion <= 4 (En Python)
        
        x = int (input("Ingrese el primer argumento: "))
        y = int (input("Ingrese el segundo argumento: "))        

    
    # Analizamos la opcion ingresada por teclado
    match opcion:
        case 1:
            print("El resultado de la suma es: ", suma(x, y))

        case 2:
            print("El resultado de la resta es: ", resta(x, y))

        case 3:
            print("El resultado de la multiplicacion es: ", multiplicar(x, y))
        
        case 4:
            print("El resultado de la division es: ", dividir(x, y))
        
        case 5:
            print("Terminando programa...")
       
        case _:
            print("ERROR: Opcion invalida.")
    
    
    # Si no elegimos la opcion de salir, llamamos nuevamente al menu principal
    # para seguir ejecutando el programa.
    if opcion != 5:
        menuPrincipal()
    

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

#? Que puede pasar cuando el segundo argumento es 0 ?
#? Se te ocurre alguna forma de solucionarlo ?
def dividir(x, y):
    return x / y



if __name__ == "__main__":
    menuPrincipal()