from modules.ColaPrioridad_alterado import ColaDePrioridad
from modules.Grafo import Grafo,Vertice
import sys

def prim(G,v_inicio):
    mejor_ruta = []
    cp = ColaDePrioridad()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)

    v_inicio.asignarDistancia(0)
    cp.cola.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        tupla_verticeActual = cp.avanzar()
        verticeActual = tupla_verticeActual[1]

        #agregamos tuplas a la mejor ruta
        if verticeActual.obtenerPredecesor():
            vertice_predecesor = verticeActual.obtenerPredecesor()
            costo = verticeActual.obtenerDistancia()
            mejor_ruta.append((vertice_predecesor.id, verticeActual.id, costo))


        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decrementarClave(verticeSiguiente,nuevoCosto)
        
    return mejor_ruta