def cargar_datos(archivo):
  try:
    file = open(archivo, "r")
  except:
    print("El archivo no existe")

  datos = {}

  for line in file:
    contenido = line.split(":")
    clave = contenido[0]
    valor = contenido[1]
    datos[clave] = valor

  file.close()

  return datos

print(cargar_datos("e6.txt"))

def guardar_datos(datos, archivo):
  try:
    file = open(archivo, "a")
  except:
    print("El archivo no existe")

  for dato in datos:
    file.write(dato + ":" + datos[dato] + "\n")
  
  file.close()

diccionario = {
  "calle": "fddsafdsaf",
  "localidad": "dffsfasd"
}

#guardar_datos(diccionario,"e6.txt")