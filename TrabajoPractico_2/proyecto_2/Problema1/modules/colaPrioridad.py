from modules.monticuloBinario import MonticuloBinario
   
class ColaDePrioridad:
    def __init__(self):
        self.__cola = MonticuloBinario("min")

    @property
    def cola(self):
        return self.__cola

    def ingresar(self,dato):
        self.__cola.insertar(dato)
    
    def avanzar(self):
        self.__cola.eliminarRaiz()
    
    def __len__(self):
        return self.__cola.tamanio
    
    def __iter__(self):
        return iter(self.__cola)

