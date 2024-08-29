# repetir :: String Number -> String
# Dada una palabra y un numero n la funcion devolvera como resultado
# un string con la palabra repetida n veces
def repetir(nombre, n):
    return nombre * n

def test_repetir():
    assert repetir("Federico", 0) == ""
    assert repetir("Federico", 1) == "Federico"
    assert repetir("Federico", 2) == "FedericoFederico"
    assert repetir("Federico", 3) == "FedericoFedericoFederico"