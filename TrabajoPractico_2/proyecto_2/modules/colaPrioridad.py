from monticuloBinario import MonticuloBinario
from paciente import Paciente
   
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

