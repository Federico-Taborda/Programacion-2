def celcius_fahrenheit(celcius:int) -> int:
    return (celcius * 9 / 5) + 32

def tabla_conversion():
    for celcius in range(0, 121):
        if celcius % 10 == 0:
            c = str(celcius)
            f = str(celcius_fahrenheit(celcius))
            print("Celcius: " + c + " => " + "Fahrenheit: " + f)

#tabla_conversion()