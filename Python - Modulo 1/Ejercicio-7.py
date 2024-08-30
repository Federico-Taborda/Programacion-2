def duplica(nombre):
    return nombre * 2

duplica("Federico")
duplica("a")

def test_duplica():
    assert duplica("a") == "aa"
    assert duplica("1") == "11"
    assert duplica("federico") == "federicofederico"
    assert duplica("lcc") == "lcclcc"
