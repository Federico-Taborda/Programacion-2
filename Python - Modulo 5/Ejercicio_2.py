def copiar(caracteres, archivo1, archivo2):
  try:
    with open(archivo1, "r") as file:
      texto = file.read(caracteres)
      agregar_linea(archivo2, texto)

  except:
    print("El archivo no existe")

def agregar_linea(archivo, linea):
  try:
    with open(archivo, "a") as file:
      file.write(linea)

  except:
    print("El archivo no existe")

def main():
  copiar(5, "e2.txt", "e2-copia.txt")
  
if __name__ == "__main__":
  main()
