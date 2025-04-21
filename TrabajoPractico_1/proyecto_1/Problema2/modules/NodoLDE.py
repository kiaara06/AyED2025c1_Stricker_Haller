class NodoLDE:
    def __init__(self,dato_inicial):
        self.__dato = dato_inicial
        self.__siguiente = None
        self.__anterior = None
    
    @property
    def dato(self):
        return self.__dato
    @property
    def siguiente(self):
        return self.__siguiente
    @property
    def anterior(self):
        return self.__anterior
    
    @dato.setter
    def dato(self,nuevo_dato):
        self.__dato = nuevo_dato
    @siguiente.setter
    def siguiente(self,nuevo_siguiente):
        self.__siguiente = nuevo_siguiente
    @anterior.setter
    def anterior(self,nuevo_anterior):
        self.__anterior = nuevo_anterior

