def cargar_datos(archivo):
  datos = {}
  try:
    with open(archivo, "r") as file:
      for line in file:
        contenido = line.split(":")
        clave = contenido[0]
        valor = contenido[1]
        datos[clave] = valor
      return datos
  except:
    print("El archivo no existe")


def guardar_datos(datos, archivo):
  try:
    with open(archivo, "a") as file:
      for dato in datos:
        file.write(dato + ":" + datos[dato] + "\n")
  except:
    print("El archivo no existe")

diccionario = {
  "calle": "fddsafdsaf",
  "localidad": "dffsfasd"
}

def main():
  guardar_datos(diccionario,"e6.txt")
  print(cargar_datos("e6.txt"))
  
if __name__ == "__main__":
  main()