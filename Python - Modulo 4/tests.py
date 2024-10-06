from Ejercicio_1 import *
from Ejercicio_2 import *
from Ejercicio_3 import *
from Ejercicio_4 import *
from Ejercicio_5 import *
from Ejercicio_6 import *
from Ejercicio_7 import *
from Ejercicio_8 import *
from Ejercicio_9 import *
from Ejercicio_10 import *
from Ejercicio_11 import *
from Ejercicio_12 import *
from Ejercicio_13 import *
from Ejercicio_14 import *

# Ejercicio 1
# Ejercicio 2

# Ejercicio 3
def test_busqueda_binaria():
    assert busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 4) == 3
    assert busqueda_binaria(["a", "b", "c", "d", "e", "f"], "b") == 1
    assert busqueda_binaria(["a", "c", "d", "e", "f"], "b") == 1

# Ejercicio 4

# Ejercicio 5

def test_cantidad_caracteres():
    assert cantidad_caracteres("") == {}
    assert cantidad_caracteres("hola") == {"h": 1, "o": 1, "l": 1, "a": 1}
    assert cantidad_caracteres("agua") == {"a": 2, "g": 1, "u": 1}

def test_apariciones_palabra():
    assert apariciones_palabra("hola hola") == {"hola": 2}
    assert apariciones_palabra("hola que tal") == {"hola": 1, "que": 1, "tal": 1}
    assert apariciones_palabra("hola hola adios") == {"hola": 2, "adios": 1}
    assert apariciones_palabra_split("hola hola") == {"hola": 2}
    assert apariciones_palabra_split("hola que tal") == {"hola": 1, "que": 1, "tal": 1}
    assert apariciones_palabra_split("hola hola adios") == {"hola": 2, "adios": 1}

# Ejercicio 6
# Ejercicio 7
# Ejercicio 8

# Ejercicio 9
def test_carrito_compras():
    assert carrito_compras({"a": 10, "b": 15, "c":5}, {"a": 1, "b": 3, "c": 2}) == 65
    assert carrito_compras({"jabon": 10, "trapo": 5}, {"jabon": 2,"trapo": 1}) == 25
    
# Ejercicio 10
# Ejercicio 11
# Ejercicio 12
# Ejercicio 13
# Ejercicio 14