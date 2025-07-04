from modules.Grafo import Vertice,Grafo
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

#ENTREGABLE 1
lista_aldeas = grafo_aldeas.obtenerVertices()
lista_aldeas_ordenadas = sorted(lista_aldeas)
print("-"*100)
print("Entregable 1")
print("-"*100)
print(f"""La listas de las aldeas, ordenadas alfabéticamente:""")
for i in range(0,len(lista_aldeas_ordenadas)-1):
   print(f"{i+1}: {lista_aldeas_ordenadas[i]}")

#ENTREGABLE 2
def imprimir_rutas_noticia(mejor_ruta):
    """
    Función que, para cada aldea, muestra de qué vecina recibe
    la noticia, y a qué vecinas envía réplicas
    """
    conexiones = {}

    for origen, destino, _ in mejor_ruta:
        if origen not in conexiones:
            conexiones[origen] = {'recibe_de': None, 'envia_a': []}
        if destino not in conexiones:
            conexiones[destino] = {'recibe_de': None, 'envia_a': []}

        # Establecer las relaciones de envío y recepción
        conexiones[origen]['envia_a'].append(destino)
        conexiones[destino]['recibe_de'] = origen 

    for aldea, info in conexiones.items():
            recibe_de_str = info['recibe_de'] if info['recibe_de'] else "ninguna, ya que es el origen de la ruta de mensajes"
            envia_a_str = ", ".join(info['envia_a']) if info['envia_a'] else "ninguna"
            print(f"La aldea '{aldea}':")
            print(f"  Recibe la noticia de: {recibe_de_str}")
            print(f"  y envía réplicas a: {envia_a_str}")
            print("-" * 100)

print("\n")
print("-"*100)
print("Entregable 2")
print("-"*100)
print("""Para cada aldea, se muestra de qué vecina recibe la noticia, y a qué vecinas envía réplicas""")
print("-"*100)
print(imprimir_rutas_noticia(Mejor_ruta))


#ENTREGABLE 3
distancia_max = 0
for tupla in Mejor_ruta:
    distancia_max += tupla[2]
print("\n")
print("-"*100)
print("Entregable 3")
print("-"*100)
print(f"""Para el envío de una noticia, la suma de todas las distancias 
recorridas por todas las palomas enviadas desde cada palomar es {distancia_max} leguas""")
print("-"*100)
