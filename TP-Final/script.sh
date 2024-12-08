#!/bin/zsh

# Script de pruebas para el archivo main.c
#gcc -Wall -Wextra -Werror ./main.c -lm && valgrind ./a.out

# Script de pruebas para el archivo main.py
#gcc -Wall -Wextra -Werror ./main.c -lm && python3 main.py

# Script para correr los test de python
pytest test_main.py