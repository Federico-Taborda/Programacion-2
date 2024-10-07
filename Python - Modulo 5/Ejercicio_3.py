def wc(archivo):
  try:
    with open(archivo, "r") as file:
      lineas = 0
      caracteres = 0
      palabras = 0

      for line in file:
        caracteres += len(line)
        lineas += 1
        palabras += len(line.split())

      return {
        "lineas": lineas,
        "palabras": palabras,
        "caracteres": caracteres
      }
  except:
    print("El archivo no existe")

def main():
  print(wc("head.txt"))
  
  
if __name__ == "__main__":
  main()