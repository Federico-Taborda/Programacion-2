def carrito_compras(precios:dict, cantidades:dict) -> int:
    total = 0

    for producto in cantidades:
        total += cantidades[producto] * precios[producto]
        
    return total