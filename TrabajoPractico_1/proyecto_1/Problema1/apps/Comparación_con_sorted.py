import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.Ordenamiento_Burbuja import ordenamiento_Burbuja
from modules.Ordenamiento_Quicksort import ordenamiento_Quicksort
from modules.Ordenamiento_Residual import ordenamiento_Residual
import random
import time
import matplotlib.pyplot as plt

tiempos_burbuja = []
tiempos_quicksort = []
tiempos_residual = []
tiempos_sorted = []

lista_tamaños = [1,100,200,300,400,500,600,700,800,900,1000]
for i in lista_tamaños:
    lista_prueba = [random.randint(0,10000) for _ in range(i)]

    copia_burbuja = lista_prueba.copy()
    inicio_b = time.perf_counter()
    ordenamiento_Burbuja(copia_burbuja)
    fin_b = time.perf_counter()
    tiempo_b = fin_b - inicio_b
    tiempos_burbuja.append(tiempo_b)

    copia_quick = lista_prueba.copy()
    inicio_q = time.perf_counter()
    ordenamiento_Quicksort(copia_quick)
    fin_q = time.perf_counter()
    tiempo_q = fin_q - inicio_q
    tiempos_quicksort.append(tiempo_q)

    copia_residual = lista_prueba.copy()
    inicio_r = time.perf_counter()
    ordenamiento_Residual(copia_residual)
    fin_r = time.perf_counter()
    tiempo_r = fin_r - inicio_r
    tiempos_residual.append(tiempo_r)

    copia_sorted = lista_prueba.copy()
    inicio_s = time.perf_counter()
    sorted(copia_residual)
    fin_s = time.perf_counter()
    tiempo_s = fin_s - inicio_s
    tiempos_sorted.append(tiempo_s)

plt.figure(figsize=(12, 11))
plt.plot(lista_tamaños, tiempos_burbuja, label="Ordenamiento Burbuja")
plt.plot(lista_tamaños, tiempos_quicksort, label="Ordenamiento Quicksort")
plt.plot(lista_tamaños, tiempos_residual, label="Ordenamiento Residual")
plt.plot(lista_tamaños, tiempos_sorted, label="Sorted")

plt.xlabel("Lista de N elementos")
plt.ylabel("Tiempo de ordenamiento (segundos)")
plt.title("Comparación de los tiempos de ejecución")
plt.xticks(lista_tamaños)
plt.legend()
plt.grid(True)
plt.show()
