# Programacion-2
Repositorio de teoria y ejercicios de la materia

## Python - Anotaciones

- Todos los tipos de datos primitivos son inmutables. Lo cual si queremos modificar un tipo de dato primitivo no sera posible, sino que estariamos creando un nuevo dato diferente.

- Utilizar slincing sobre listas no modifica la lista en si, sino que se crea una nueva lista y ocupando mas espacio en memoria.

- Una funcion en la que no se declara que valor retorna entonces su valor es None

- La funciones recursivas que llevan los resultados en los argumentos de la funcion se llaman recursion en cola

- Todas las funciones recursivas se pueden hacer iterativas y viceversa. Pero no siempre el costo de una funcion recursiva sera menor que una iterativa.

- Es una mala practica en las funciones interrupir los bucles con un return. No se deberia forzar la salida del ciclo. Los bucles deben terminar solo si la condicion del bucle es falsa.

- Python nos permite escribir la signatura de las funciones en el mismo codigo. Esto no es necesario pero ayuda a ver con que tipos datos recibe la funcion y que retorna.

```
cualquier_tipo_de_dato:any

cadenas:str
numeros_entero:int
numeros_decimal:float
numeros_complejo:complex
booleanos:bool

listas:list
tuplas:tuple

diccionarios:dict
conjuntos:set

# Ejemplo
def mi_funcion(cadena:str, numero:int, lista:list) -> int:

```

# Ejecutar tests

## Python test

Para ejecutar los test de los modulos de python ejecutar el bash python_test.sh

```
// Ejecuta los test de un modulo en especifico
bash python_test.sh [numero del modulo]

// Ejecuta los test de todos los modulos
bash python_test.sh

```

# Compilar los ejercicios de C

Para compilar un ejercicio de los modulos de C se puede hacer de dos maneras

```
// Compila un ejercicio si estas en el mismo directorio del archivo
gcc -Wall -o [nombre del ejercicio]

// Compila un ejercicio dado de un modulo dado y lo ejecuta
bash compilar.sh [numero de modulo] [nombre del ejercicio]

```