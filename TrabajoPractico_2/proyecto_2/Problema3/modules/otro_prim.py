from modules.colaDePrioridadPrim import ColaDePrioridadPrim
from modules.Grafo import Grafo, Vertice
import sys

def prim2(G,v_inicio):
    mejor_ruta = []
    cp = ColaDePrioridadPrim()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)

    v_inicio.asignarDistancia(0)
    id_vertices = []
    for v in G:
        id_vertices.append((v.obtenerDistancia(), v))

    cp.cola.construirMonticulo_prim(id_vertices)
    vertices_en_mst = set() #rastrea nodos visitados

    while not cp.estaVacia():
        distancia_actual, verticeActual = cp.avanzar()
        if verticeActual in vertices_en_mst:
            continue
        vertices_en_mst.add(verticeActual) #lo marca como visitado

        #si tiene predecesor, ya es parte de mst
        if verticeActual.obtenerPredecesor():
            vertice_predecesor = verticeActual.obtenerPredecesor()
            costo = verticeActual.obtenerDistancia() 
            mejor_ruta.append((vertice_predecesor.id, verticeActual.id, costo))

        for verticeSiguiente in verticeActual.obtenerConexiones():
            if verticeSiguiente not in vertices_en_mst:
                nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
                
                if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    verticeSiguiente.asignarDistancia(nuevoCosto)
                    cp.decrementarClave(verticeSiguiente, nuevoCosto)

    return mejor_ruta

