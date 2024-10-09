def ej14(dic):
    a = set(range(1,31))
    for element in dic:
        b = set(dic[element])
        a = a.intersection(b)
        # a = a & b
    return a

def organizar_reunion(dic):
    dias_comunes = {"Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"}
    for _, dias in dic.items():
        dias_comunes &= set(dias)
    return dias_comunes

def main():
    d = {
        "juan":   ["Lunes",  "Miercoles", "Viernes"],
        "seba":   ["Lunes",  "Viernes",   "Sabado"],
        "joaco":  ["Lunes",  "Viernes"],
        "martin": ["Martes", "Jueves",    "Viernes"],
        "valen":  ["Martes", "Viernes",   "Sabado"],
        "bauti":  ["Lunes",  "Martes",    "Miercoles", "Jueves", "Viernes", "Sabado"]
    }
    
    print("Los dias posibles son: ",organizar_reunion(d))

if __name__ == "__main__":
    main()
    
