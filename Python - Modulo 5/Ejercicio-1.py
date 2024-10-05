def leer_lineas(archivo, n):
  try:
    file = open(archivo, "r")
  except:
    print("El archivo no existe")

  while n > 0:
    linea = file.readline()
    print(linea)
    n -= 1

  file.close()

leer_lineas("head.txt", 2)