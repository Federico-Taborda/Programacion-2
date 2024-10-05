def copiar(caracteres, archivo1, archivo2):
  try:
    file = open(archivo1, "r")
  except:
    print("El archivo no existe")
  
  texto = file.read(caracteres)
  agregar_linea(archivo2, texto)
  
  file.close()

def agregar_linea(archivo, linea):
  try:
    file = open(archivo, "a")
  except:
    print("El archivo no existe")
  
  file.write(linea)
  file.close()

#copiar(5, "prueba.txt", "prueba2.txt")