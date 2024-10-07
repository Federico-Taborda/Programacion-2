def grep(expresion, archivo):
  try:
    with open(archivo, "r") as file:
      for linea in file:
        if expresion in linea:
          print(linea)
  except:
    print("El archivo no existe")

def main():
  grep("pr", "e4.txt")
  
if __name__ == "__main__":
  main()