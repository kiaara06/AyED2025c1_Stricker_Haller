class Vertice:
    def __init__(self,clave):
        import sys
        if isinstance(clave,str):
            self.__id = clave
        else:
            raise TypeError("La clave debe ser un string")
        self.__conectadoA = {}
        self.__distancia = sys.maxsize
        self.__predecesor = None

    @property
    def id(self):
        return self.__id
    
    def __lt__(self, otro_vertice):
        """
        Define el comportamiento del operador menor que (<).
        Compara vértices alfabéticamente basándose en su ID.
        """
        if not isinstance(otro_vertice, Vertice):
            raise TypeError ("Se debe pasar otro objeto Vertice")
        return self.__id < otro_vertice.__id

    def __gt__(self, otro_vertice):
        """
        Define el comportamiento del operador mayor que (>).
        Compara vértices alfabéticamente basándose en su ID.
        """
        if not isinstance(otro_vertice, Vertice):
            return TypeError ("Se debe pasar otro objeto Vertice")
        return self.__id > otro_vertice.__id
    
    def __eq__(self, otro_vertice):
        """
        Permite la comparacion de objetos Vertice
        """
        if not isinstance(otro_vertice, Vertice):
            return False
        return self.__id == otro_vertice.__id

    def __hash__(self):
        """
        Este método devuelve un valor hash entero para el objeto (su identificador, o clave)
        """
        return hash(self.__id)

    def agregarVecino(self,vecino,ponderacion=0):
        """
        Agrega una conexión desde este vértice a otro.
        """
        if isinstance(vecino,Vertice):
            self.__conectadoA[vecino] = ponderacion
        else:
            raise TypeError("El vecino debe ser un objeto tipo Vertice")

    def __str__(self):
        """
        Define la representación de un objeto como cadena. 
        """
        return str(self.__id) + ' conectadoA: ' + str([x.id for x in self.__conectadoA])

    def obtenerConexiones(self):
        """
        Devuelve todos los vértices de la lista de adyacencia, representados por la variable conectadoA.
        """
        return self.__conectadoA.keys()


    def obtenerPonderacion(self,vecino):
        """
        Permite obtener el peso de la conexión a un vecino específico.
        """
        return self.__conectadoA[vecino]
    
    def asignarDistancia(self,una_distancia):
        self.__distancia = una_distancia
    
    def obtenerDistancia(self):
        return self.__distancia
    
    def asignarPredecesor(self,un_predecesor):
        self.__predecesor = un_predecesor
    
    def obtenerPredecesor(self):
        return self.__predecesor

class Grafo:
    def __init__(self):
        self.__listaVertices = {}
        self.__numVertices = 0

    def agregarVertice(self,clave):
        """
        Agrega un nuevo vértice al grafo.
        """
        self.__numVertices = self.__numVertices + 1
        nuevoVertice = Vertice(clave)
        self.__listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,id):
        """
        Recupera un objeto Vértice del grafo utilizando su id.
        """
        if id in self.__listaVertices:
            return self.__listaVertices[id]
        else:
            return None

    def __contains__(self,id):
        """
        Método que permite usar el operador in. Devuelve True or False.
        """
        return id in self.__listaVertices

    def agregarArista(self,de,a,ponderacion=0):
        """
        Define conexiones (bordes o "aristas") entre vértices en el grafo.
        """
        if de not in self.__listaVertices: 
            #Comprueba si el vértice "de" ya existe en el grafo. De no ser así, lo añade automáticamente.
            nuevo_vertice = self.agregarVertice(de)

        if a not in self.__listaVertices:
            #Comprueba si el vértice "a" ya existe en el grafo. De no ser así, lo añade automáticamente.
            nuevo_vertice = self.agregarVertice(a)

        self.__listaVertices[de].agregarVecino(self.__listaVertices[a], ponderacion)

    def obtenerVertices(self):
        """
        Devuelve una vista de todos los id de vértices (claves) presentes actualmente en el grafo.
        """
        return self.__listaVertices.keys()

    def __iter__(self):
        """
        Permite la iteración sobre todos los objetos Vertice del grafo mediante un ciclo for. 
        """
        return iter(self.__listaVertices.values())