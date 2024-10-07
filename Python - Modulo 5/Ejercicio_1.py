def leer_lineas(archivo, n):
  try:
    with  open(archivo, "r") as file:
      while n > 0:
        linea = file.readline()
        print(linea)
        n -= 1

  except FileNotFoundError:
    print("El archivo no existe")
    return

def main():
  leer_lineas("head.txt", 2)

if __name__ == "__main__":
  main()