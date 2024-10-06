def solicitar_positivo():
    numero = int(input("Ingrese un numero positivo: "))

    while not numero > 0:
        print("Vuelva a intentarlo")
        return solicitar_positivo()
    
    return print("Es positivo")

#solicitar_positivo()