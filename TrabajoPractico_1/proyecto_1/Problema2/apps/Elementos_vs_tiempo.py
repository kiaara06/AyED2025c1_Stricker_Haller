# Aplicación para la gráfica del problema 2

from modules.ListaDobleEnlazada import ListaDobleEnlazada
import random
import time
import matplotlib.pyplot as plt
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

lista_tamaños = [1,10,20,30,40,50,60,70,80,90,100]
for i in lista_tamaños:
    lista_prueba = ListaDobleEnlazada()
    for _ in range(i): 
        lista_prueba.agregar_al_final(random.randint(0,100))

    inicio_len = time.perf_counter()
    len(lista_prueba)
    fin_len = time.perf_counter()
    t_len = fin_len - inicio_len
    tiempos_len.append(t_len)

    inicio_copiar = time.perf_counter()
    c2 = lista_prueba.copiar()
    fin_copiar = time.perf_counter()
    t_copiar = fin_copiar - inicio_copiar
    tiempos_copiar.append(t_copiar)

    inicio_invertir = time.perf_counter()
    lista_prueba.invertir()
    fin_invertir = time.perf_counter()
    t_invertir = fin_invertir - inicio_invertir
    tiempos_invertir.append(t_invertir)

plt.figure(figsize=(12, 11))
plt.plot(lista_tamaños, tiempos_len, label="método len")
plt.plot(lista_tamaños, tiempos_copiar, label="método copiar")
plt.plot(lista_tamaños, tiempos_invertir, label="método invertir")

plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de tiempos de ejecución de 3 métodos de las ListasDobleEnlazadas")
plt.xticks(lista_tamaños)
plt.legend()
plt.grid(True)
plt.show()

