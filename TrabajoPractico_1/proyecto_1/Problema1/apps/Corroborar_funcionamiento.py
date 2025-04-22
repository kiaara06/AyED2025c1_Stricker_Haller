import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.Ordenamiento_Burbuja import ordenamiento_Burbuja
from modules.Ordenamiento_Quicksort import ordenamiento_Quicksort
from modules.Ordenamiento_Residual import ordenamiento_Residual

#GENERAMOS UNA LISTA ALEATORIA DE 500 NÚMEROS DE 5 DÍGITOS:
lista_original = [random.randint(10000, 99999) for _ in range(500)]

#Para verificar el correcto funcionamiento de los algoritmos implementados, 
#los probamos con la lista aleatoria

# Burbuja
lista_burbuja = ordenamiento_Burbuja(lista_original.copy())

# Quicksort
lista_quicksort = ordenamiento_Quicksort(lista_original.copy())

# Radix (residual)
lista_residual = ordenamiento_Residual(lista_original.copy())

if lista_burbuja == lista_quicksort and lista_quicksort == lista_residual:
    print(f"""Los algoritmos de ordenamiento funcionan""")
else:
    print(f"Los algoritmos de ordenamiento no funcionan")
