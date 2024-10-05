def wc(archivo):
  try:
    file = open(archivo, "r")
  except:
    print("El archivo no existe")

  lineas = 0
  caracteres = 0
  palabras = 0

  for line in file:
    caracteres += len(line)
    lineas += 1
    palabras += len(line.split())
  
  file.close()

  return {
    "lineas": lineas,
    "palabras": palabras,
    "caracteres": caracteres
  }

#print(wc("prueba.txt"))
