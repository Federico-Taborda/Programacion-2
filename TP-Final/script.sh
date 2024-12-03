#!/bin/zsh

# Script de pruebas para el archivo main.c
gcc -Wall -Wextra -Werror ./main.c -lm && valgrind ./a.out