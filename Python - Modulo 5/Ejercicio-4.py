def grep(expresion, archivo):
  try:
    file = open(archivo, "r")
  except:
    print("El archivo no existe")
  
  for linea in file:
    if expresion in linea:
      print(linea)
  file.close()

grep("pr", "e4.txt")