def carrito_compras(precios, cantidades):
    total = 0

    for producto in cantidades:
        total += cantidades[producto] * precios[producto]
        
    return total

def test_carrito_compras():
    assert carrito_compras({"a": 10, "b": 15, "c":5}, {"a": 1, "b": 3, "c": 2}) == 65
    assert carrito_compras({"jabon": 10, "trapo": 5}, {"jabon": 2,"trapo": 1}) == 25