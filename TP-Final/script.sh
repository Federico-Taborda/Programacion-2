#!/bin/zsh

gcc -Wall -Wextra -Werror -o ejecutable ./main.c -lm && valgrind ./ejecutable