from modules.monticuloBinarioPrim import MonticuloBinarioPrim
   
class ColaDePrioridadPrim:
    def __init__(self):
        self.__cola = MonticuloBinarioPrim("min")

    @property
    def cola(self):
        return self.__cola

    def ingresar(self,tupla): #se cambió (self,dato) a (self,tupla), ya que se requiere (prioridad, elemento) 
        self.__cola.insertar(tupla)
    
    def avanzar(self):
        tupla_eliminada = self.__cola.eliminarRaiz()
        return tupla_eliminada
    
    def __len__(self):
        return self.__cola.tamanio
    
    def __iter__(self):
        return iter(self.__cola)
    
    def estaVacia(self): 
        return self.__cola.estaVacio()
    
    def decrementarClave(self, clave_existente_vertice, nueva_clave_distancia):
        """
        Disminuye la clave de un elemento existente en el montículo.
        clave_existente_vertice: el vértice
        nueva_clave_distancia: nueva distancia
        """
        self.__cola.decrementarClave(clave_existente_vertice, nueva_clave_distancia)

    def __contains__(self, elemento):
        return self.__cola.buscar(elemento)