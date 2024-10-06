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
def test_apariciones():
    assert apariciones([], "a") == 0
    assert apariciones(["a"], "a") == 1
    assert apariciones(["a", "a", "c"], "a") == 2
    assert apariciones([], 1) == 0
    assert apariciones([1, 1, 2, 1], 1) == 3

def test_apariciones_recursivo():
    assert apariciones_recursivo([], "a") == 0
    assert apariciones_recursivo(["a"], "a") == 1
    assert apariciones_recursivo(["a", "a", "c"], "a") == 2
    assert apariciones_recursivo([], 1) == 0
    assert apariciones_recursivo([1, 1, 2, 1], 1) == 3

def test_primera_coincidencia():
    assert primera_coincidencia([], "a") == -1
    assert primera_coincidencia(["a"], "a") == 0
    assert primera_coincidencia(["b", "a", "c"], "a") == 1
    assert primera_coincidencia([], 1) == -1
    assert primera_coincidencia([1, 1, 2, 1], 1) == 0
    assert primera_coincidencia([4, 3, 2, 1], 1) == 3

def test_primera_coincidencia_recursivo():
    assert primera_coincidencia_recursivo([], "a") == -1
    assert primera_coincidencia_recursivo(["a"], "a") == 0
    assert primera_coincidencia_recursivo(["b", "a", "c"], "a") == 1
    assert primera_coincidencia_recursivo([], 1) == -1
    assert primera_coincidencia_recursivo([1, 1, 2, 1], 1) == 0
    assert primera_coincidencia_recursivo([4, 3, 2, 1], 1) == 3
    assert primera_coincidencia_recursivo([4, 3, 2, 1], 5) == -1

def test_lista_apariciones():
    assert lista_apariciones([], "a") == []
    assert lista_apariciones(["a"], "a") == [0]
    assert lista_apariciones(["b", "a", "a"], "a") == [1, 2]
    assert lista_apariciones([], 1) == []
    assert lista_apariciones([1, 1, 2, 1], 1) == [0, 1, 3]
    assert lista_apariciones([4, 3, 2, 1], 1) == [3]

def test_lista_apariciones_recursivo():
    assert lista_apariciones([], "a") == []
    assert lista_apariciones(["a"], "a") == [0]
    assert lista_apariciones(["b", "a", "a"], "a") == [1, 2]
    assert lista_apariciones([], 1) == []
    assert lista_apariciones([1, 1, 2, 1], 1) == [0, 1, 3]
    assert lista_apariciones([4, 3, 2, 1], 1) == [3]

# Ejercicio 2
def test_valor_maximo_uno():
    assert valor_maximo_uno([1]) == 1
    assert valor_maximo_uno([1,2,3]) == 3
    assert valor_maximo_uno([3,4,7,2,5,1,3]) == 7
    assert valor_maximo_uno([3,4,7,7,5,1,3]) == 7
    assert valor_maximo_uno([3,4,7,2,5,1,3,5,8,11,2,55]) == 55
    assert valor_maximo_uno(["a", "b", "c"]) ==  "c"
    assert valor_maximo_uno(["s", "m", "a"]) ==  "s"

def test_valor_maximo_dos():
    assert valor_maximo_dos([1]) == (1, 0)
    assert valor_maximo_dos([1,2,3]) == (3, 2)
    assert valor_maximo_dos([3,4,7,2,5,1,3]) == (7, 2)
    assert valor_maximo_dos([3,4,7,2,55]) == (55, 4)
    assert valor_maximo_dos(["a", "b", "c"]) ==  ("c", 2)
    assert valor_maximo_dos(["s", "m", "a"]) ==  ("s", 0)

# Ejercicio 3
def test_busqueda_binaria():
    assert busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 4) == 3
    assert busqueda_binaria(["a", "b", "c", "d", "e", "f"], "b") == 1

# Ejercicio 4
def test_lista_a_diccionario():
    assert lista_a_diccionario([("a", 1), ("a", 2), ("b", 3), ("b", 4)]) == {
        "a": [1,2],
        "b": [3,4]
    }
    assert lista_a_diccionario([("Hola", "don pepito"), ("Hola", "don jose"), ("Buenos", "dias")]) == {
        "Hola": ["don pepito", "don jose"],
        "Buenos": ["dias"]
    }

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
def test_caracter_palabra():
    assert caracter_palabra("a bc") == {"a": "a", "b": "bc", "c": "bc"}
    assert caracter_palabra("la letra en la palabra mas larga") == {
        "l": "palabra",
        "a": "palabra",
        "m": "mas",
        "e": "letra",
        "r": "palabra",
        "b": "palabra",
        "t": "letra",
        "n": "en",
        "s": "mas",
        "g": "larga",
        "p": "palabra"
    }

# Ejercicio 7
def test_promedio():
    notas = {"Federico": [1, 1, 6], "Gabriel": [7, 7, 8], "Ezequiel": [8, 8, 8]}
    assert promedio(notas) == {"Federico": 2,"Gabriel": 7,"Ezequiel": 8}

def test_mayor_promedio():
    notas = {"Federico": [1, 1, 6], "Gabriel": [7, 7, 8], "Ezequiel": [8, 8, 8]}
    assert mayor_promedio(notas) == "Ezequiel"
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