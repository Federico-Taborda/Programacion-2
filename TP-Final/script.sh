#!/bin/zsh

gcc -Wall -Wextra -o ejecutable ./main.c -lm && valgrind ./ejecutable