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

# Ejercicio 1
def test_posiciones_multiplo():
    assert posiciones_multiplo([1,2,3,4,5,6,7],2) == [1, 3, 5]
    assert posiciones_multiplo([1,2,3,4,5,6,7],3) == [2, 5]

def test_posiciones_multiplo_recursiva():
    assert posiciones_multiplo_recursiva([1,2,3,4,5,6,7],2) == [1, 3, 5]
    #assert posiciones_multiplo_recursiva([1,2,3,4,5,6,7],3) == [2, 3]

# Ejercicio 2
def test_acumular():
    assert acumular_for([1,2,3]) == [1,3,6]
    assert acumular_for([1,1,1]) == [1,2,3]
    assert acumular_while([1,2,3]) == [1,3,6]
    assert acumular_while([1,1,1]) == [1,2,3]

def test_acumular_recursivo():
    assert acumular_recursivo([1,2,3]) == [1,3,6]

# Ejercicio 3
def test_elimina():
    assert elimina_uno([1,2,3]) == [2]  
    assert elimina_dos([1,2,3]) == [2]
    assert elimina_tres([1,2,3]) == [2]
    assert elimina_cuatro([1,2,3]) == [2]

# Ejercicio 4
def test_ordenada():
    assert ordenada([1,2,3]) == True
    assert ordenada([4,2,3]) == False
    assert ordenada(["a", "b", "c"]) == True
    assert ordenada(["b", "a", "c"]) == False

# Ejercicio 5
def test_duplicado():
    assert duplicado([1,2,3,4]) == False
    assert duplicado([1,2,3,4,4]) == True
    assert duplicado(["a", "a", "a"]) == True
    assert duplicado_recursivo([1,2,3,4]) == False
    assert duplicado_recursivo([1,2,3,4,4]) == True
    assert duplicado_recursivo(["a", "a", "a"]) == True

# Ejercicio 6
def test_elimina_duplicado():
    assert elimina_duplicado_for([]) == []
    assert elimina_duplicado_for(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_for([1, 1, 1]) == [1]
    assert elimina_duplicado_dos([]) == []
    assert elimina_duplicado_dos(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_dos([1, 1, 1]) == [1]
    assert elimina_duplicado_recursivo([]) == []
    #assert elimina_duplicado_recursivo(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_recursivo([1, 1, 1]) == [1]
    assert elimina_duplicado_conjuntos([]) == []
    #assert elimina_duplicado_conjuntos(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_conjuntos([1, 1, 1]) == [1]

# Ejercicio 7

# Ejercicio 8
def test_busqueda_dicotomica():
    assert busqueda_dicotomica([], "a") == False
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "c") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "e") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "h") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "i") == False
    assert busqueda_dicotomica_dos([], "a") == False
    assert busqueda_dicotomica_dos(["a", "b", "c", "d", "e", "f", "g", "h"], "c") == True
    assert busqueda_dicotomica_dos(["a", "b", "c", "d", "e", "f", "g", "h"], "e") == True
    assert busqueda_dicotomica_dos(["a", "b", "c", "d", "e", "f", "g", "h"], "h") == True
    assert busqueda_dicotomica_dos(["a", "b", "c", "d", "e", "f", "g", "h"], "i") == False
    assert busqueda_dicotomica_tres([], "a") == False
    #assert busqueda_dicotomica_tres(["a", "b", "c", "d", "e", "f", "g", "h"], "c") == True
    #assert busqueda_dicotomica_tres(["a", "b", "c", "d", "e", "f", "g", "h"], "e") == True
    #assert busqueda_dicotomica_tres(["a", "b", "c", "d", "e", "f", "g", "h"], "h") == True
    assert busqueda_dicotomica_tres(["a", "b", "c", "d", "e", "f", "g", "h"], "i") == False
    assert busqueda_dicotomica_while([], "a") == False
    assert busqueda_dicotomica_while(["a", "b", "c", "d", "e", "f", "g", "h"], "c") == True
    assert busqueda_dicotomica_while(["a", "b", "c", "d", "e", "f", "g", "h"], "e") == True
    assert busqueda_dicotomica_while(["a", "b", "c", "d", "e", "f", "g", "h"], "h") == True
    assert busqueda_dicotomica_while(["a", "b", "c", "d", "e", "f", "g", "h"], "i") == False

# Ejercicio 9
def test_mostrar_caracteres():
    assert mostrar_caracteres("hola")
    assert mostrar_caracteres_for("hola")
    assert mostrar_caracteres_while("hola")
    assert mostrar_caracteres_recursivo("hola")

# Ejercicio 10
def test_contar():
    assert contar("a", "") == 0
    assert contar("e", "palabra") == 0
    assert contar("a", "palabra") == 3
    assert contar_for("a", "") == 0
    assert contar_for("e", "palabra") == 0
    assert contar_for("a", "palabra") == 3
    assert contar_while("a", "") == 0
    assert contar_while("e", "palabra") == 0
    assert contar_while("a", "palabra") == 3
    assert contar_recursiva("a", "") == 0
    assert contar_recursiva("e", "palabra") == 0
    assert contar_recursiva("a", "palabra") == 3

# Ejercicio 11

# Ejercicio 12
def test_contar_palabras():
    assert contar_palabras_for("tengo guardado mucho dinero en mi casa") == 2
    assert contar_palabras_for("hola mundo") == 0
    #assert contar_palabras_for("letras") == 1

# Ejercicio 13

# Ejercicio 14

# Ejercicio 15