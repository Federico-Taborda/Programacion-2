from Ejercicio_1 import *
from Ejercicio_2 import *
from Ejercicio_3 import *
from Ejercicio_4 import *
from Ejercicio_5 import *
from Ejercicio_6 import *
from Ejercicio_7 import *
from Ejercicio_8 import *
from Ejercicio_9 import *

# Ejercicio 4
def test_imprimir_sumar():
    assert imprimir_suma(0) == 1275

# Ejercicio 5
def test_imprimir_sumar():
    assert imprimir_sumar(0) == 0
    assert imprimir_sumar(1) == 1
    assert imprimir_sumar(5) == 15
    assert imprimir_sumar(10) == 55

def test_imprimir_sumar_dos():
    pass
    #assert imprimir_suma_dos(0) == 0
    #assert imprimir_suma_dos(1) == 1
    #assert imprimir_suma_dos(5) == 15
    #assert imprimir_suma_dos(10) == 55
    
def test_imprimir_sumar_for():
    #assert imprimir_suma_for(0) == 0
    #assert imprimir_suma_for(1) == 1
    #assert imprimir_suma_for(5) == 15
    #assert imprimir_suma_for(10) == 55
    pass

# Ejercicio 6
def test_imprimir_suma():
    assert imprimir_suma(1, 4) == 5
    assert imprimir_suma(0, 4) == 6
    assert imprimir_suma(0, 1) == 0
    assert imprimir_suma(0, 0) == 0

def test_imprimir_suma_dos():
    assert imprimir_suma_dos(1, 4) == 5
    assert imprimir_suma_dos(0, 4) == 6
    assert imprimir_suma_dos(0, 1) == 0
    assert imprimir_suma_dos(0, 0) == 0

def test_imprimir_suma_for():
    assert imprimir_suma_for(1, 4) == 5
    assert imprimir_suma_for(0, 4) == 6
    assert imprimir_suma_for(0, 1) == 0
    assert imprimir_suma_for(0, 0) == 0

# Ejercicio 7
def test_duplica():
    assert duplica("a") == "aa"
    assert duplica("1") == "11"
    assert duplica("federico") == "federicofederico"
    assert duplica("lcc") == "lcclcc"

# Ejercicio 8
def test_repetir():
    assert repetir("Federico", 0) == ""
    assert repetir("Federico", 1) == "Federico"
    assert repetir("Federico", 2) == "FedericoFederico"
    assert repetir("Federico", 3) == "FedericoFedericoFederico"