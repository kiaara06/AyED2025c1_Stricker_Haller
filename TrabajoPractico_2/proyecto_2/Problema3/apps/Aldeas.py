from modules.grafo import Vertice,Grafo
from modules.prim import prim
import sys
import os

current_script_dir = os.path.dirname(__file__)
file_aldeas_path = os.path.join(current_script_dir, '..', 'data', 'aldeas.txt')

grafo_aldeas = Grafo()

with open(file_aldeas_path,"r",encoding="utf-8") as archi: 
    for linea in archi:
        linea = linea.strip()

        aldea_inicial,aldea_final,distancia = linea.split(",")
        
        aldea_inicial = aldea_inicial.strip()
        aldea_final = aldea_final.strip()
        distancia = int(distancia.strip())    

        grafo_aldeas.agregarArista(aldea_inicial, aldea_final, distancia)


vertice_inicio = grafo_aldeas.obtenerVertice("Peligros")
if not vertice_inicio:
    print("Error: La aldea 'Peligros' no se encontró en el grafo.")

Mejor_ruta = prim(grafo_aldeas,vertice_inicio)
for tupla in Mejor_ruta:
    print(tupla)
