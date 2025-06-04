#Probamos el correcto funcionamiento de las clases Vertice y Grafo
from modules.grafo import Vertice,Grafo

g = Grafo()

for i in range(6):
   clave = str(i)
   g.agregarVertice(clave)

g.agregarArista("0","1",5)
g.agregarArista("0","5",2)
g.agregarArista("1","2",4)
g.agregarArista("2","3",9)
g.agregarArista("3","4",7)
g.agregarArista("3","5",3)
g.agregarArista("4","0",1)
g.agregarArista("5","4",8)
g.agregarArista("5","2",1)

for v in g:
   for w in v.obtenerConexiones():
       print("( %s , %s )" % (v.id, w.id))
