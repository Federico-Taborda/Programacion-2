#!/bin/bash
if [ $1 -eq 1 ]; then
    python3 -m pytest ./'Python - Modulo 1'/tests.py
elif [ $1 -eq 2 ]; then
    python3 -m pytest ./'Python - Modulo 2'/tests.py
elif [ $1 -eq 3 ]; then
    python3 -m pytest ./'Python - Modulo 3'/tests.py
elif [ $1 -eq 4 ]; then
    python3 -m pytest ./'Python - Modulo 4'/tests.py
else
    python3 -m pytest ./'Python - Modulo 1'/tests.py
    python3 -m pytest ./'Python - Modulo 2'/tests.py
    python3 -m pytest ./'Python - Modulo 3'/tests.py
    python3 -m pytest ./'Python - Modulo 4'/tests.py
fi