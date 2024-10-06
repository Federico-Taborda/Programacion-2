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
# Ejercicio 2
# Ejercicio 3

# Ejercicio 4
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6

# Ejercicio 5

# Ejercicio 6
def test_numero_triangular():
    assert numero_triangular_for(1) == 1
    assert numero_triangular_for(2) == 3
    assert numero_triangular_for(3) == 6
    assert numero_triangular_for(4) == 10
    assert numero_triangular_for(5) == 15
    
# Ejercicio 7
# Ejercicio 8
# Ejercicio 9
# Ejercicio 10
# Ejercicio 11
# Ejercicio 12

# Ejercicio 13
def test_es_potencia():
    assert es_potencia_de_dos_for(2) and es_potencia_de_dos_while(2) and es_potencia_de_dos_recursivo(2) == True
    assert es_potencia_de_dos_for(64) == True
    assert es_potencia_de_dos_while(64) == True
    assert es_potencia_de_dos_recursivo(64) == True

def test_devolver_suma():
    assert devolver_suma(1, 10) == 15
    assert devolver_suma(2, 10) == 14
    assert devolver_suma(32, 33) == 32
    assert devolver_suma(32, 65) == 96
    
# Ejercicio 14
# Ejercicio 15