from monticuloBinario import MonticuloBinario
from paciente import Paciente
   
class ColaDePrioridad(MonticuloBinario):
    def __init__(self):
        self.__cola = MonticuloBinario("min")

    def ingresar(self,dato):
        self.__cola.insertar(dato)

h = ColaDePrioridad()
for i in range(4):
    h.ingresarPaciente()

