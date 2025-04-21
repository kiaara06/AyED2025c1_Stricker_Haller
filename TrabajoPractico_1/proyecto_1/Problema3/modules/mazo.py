# mazo.py
from modules.carta import Carta
from modules.ListaDobleEnlazada import ListaDobleEnlazada 

class DequeEmptyError(Exception):
    def __init__(self, message="El mazo está vacío"):
        self.message = message
        super().__init__(self.message)

class Mazo(ListaDobleEnlazada):
    def __init__(self):
        super().__init__() #Hereda la lista doble enlazada
    
    def poner_carta_arriba(self,carta):
        if isinstance(carta,Carta): 
            return self.agregar_al_inicio(carta)
        else:
            raise TypeError("el dato debe ser un objeto de tipo Carta")
    
    def poner_carta_abajo(self,carta):
        if isinstance(carta,Carta): 
            return self.agregar_al_final(carta)
        else:
            raise TypeError("el dato debe ser un objeto de tipo Carta")
    
    def sacar_carta_arriba(self,mostrar=False):
        if self.estaVacia():
            raise DequeEmptyError()
        else:
            carta_extraida = self.extraer(0) 
            if mostrar:
                carta_extraida.visible = True 
            return carta_extraida


