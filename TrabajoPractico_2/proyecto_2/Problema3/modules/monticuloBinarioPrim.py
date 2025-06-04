from modules.monticuloBinario import MonticuloBinario

class MonticuloBinarioPrim(MonticuloBinario):
    """
    Hijo de la clase MonticuloBinario, adaptado a cumplir las necesidades
    del algorítomo prim
    """
    def __init__(self,tipo_de_monticulo):
        super().__init__(tipo_de_monticulo)
        self.__tipo = tipo_de_monticulo.lower()

    def insertar_prim(self,tupla_clave_y_elemento): #cambio necesario (self,clave) a (self,tupla)
        """
        Inserta una tupla (clave,elemento)
        """
        self.__lista.append(tupla_clave_y_elemento)
        self._MonticuloBinario__tamanio += 1 # Acceder a __tamanio del padre
        self.infiltrarArriba_prim(self._MonticuloBinario__tamanio) # Acceder a __tamanio del padre

    def infiltrarArriba_prim(self,i):
        while i // 2 > 0:
            #Se cambió if self.__lista[i] < self.__lista[i//2]:
                #Por if self.__lista[i][0] < self.__lista[i//2][0]:
            #Se cambió if self.__lista[i] > self.__lista[i//2]:
                #Por if self.__lista[i][0] > self.__lista[i//2][0]:
            if (self.__tipo == "min" and self._MonticuloBinario__lista[i][0] < self._MonticuloBinario__lista[i//2][0]) or\
            (self.__tipo == "max" and self._MonticuloBinario__lista[i][0] > self._MonticuloBinario__lista[i//2][0]):
                
                temp = self._MonticuloBinario__lista[i//2] # Acceder a __lista del padre
                self._MonticuloBinario__lista[i//2] = self._MonticuloBinario__lista[i] # Acceder a __lista del padre
                self._MonticuloBinario__lista[i] = temp # Acceder a __lista del padre
            
            else:
                break
            i = i//2


    def infiltrarAbajo_prim(self,i):
        while (i * 2) <= self._MonticuloBinario__tamanio: # Acceder a __tamanio del padre
            hijo_menor = i * 2
            if (i * 2 + 1) <= self._MonticuloBinario__tamanio: # Acceder a __tamanio del padre
                #Se cambió if self.__lista[i * 2 + 1] < self.__lista[hijo_menor]:
                    #Por if self.__lista[i * 2 + 1][0] < self.__lista[hijo_menor][0]:
                #Se cambió if self.__lista[i * 2 + 1] > self.__lista[hijo_menor]:
                    #Por if self.__lista[i * 2 + 1][0] > self.__lista[hijo_menor][0]:
                if (self.__tipo == "min" and self._MonticuloBinario__lista[i * 2 + 1][0] < self._MonticuloBinario__lista[hijo_menor][0]) or\
                (self.__tipo == "max" and self._MonticuloBinario__lista[i * 2 + 1][0] > self._MonticuloBinario__lista[hijo_menor][0]):
                    
                    hijo_menor = i * 2 + 1

            #Se cambió if self.__lista[i] > self.__lista[hijo_menor]:
                #Por if self.__lista[i][0] > self.__lista[hijo_menor][0]:
            #Se cambió if self.__lista[i] < self.__lista[hijo_menor]:
                #Por if self.__lista[i][0] < self.__lista[hijo_menor][0]:

            if (self.__tipo == "min" and self._MonticuloBinario__lista[i][0] > self._MonticuloBinario__lista[hijo_menor][0]) or\
            (self.__tipo == "max" and self._MonticuloBinario__lista[i][0] < self._MonticuloBinario__lista[hijo_menor][0]):
                
                temp = self._MonticuloBinario__lista[i] # Acceder a __lista del padre
                self._MonticuloBinario__lista[i] = self._MonticuloBinario__lista[hijo_menor] # Acceder a __lista del padre
                self._MonticuloBinario__lista[hijo_menor] = temp # Acceder a __lista del padre
            
            else:
                break
            
            i = hijo_menor

    def construirMonticulo_prim(self,lista_de_tuplas):
        """
        Construye un montículo a partir de una lista de elementos (prioridad, item).
        Utiliza el algoritmo de heapify para construir el montículo de forma eficiente.
        """
        self._MonticuloBinario__lista = [None] # Acceder a __lista del padre y resetear
        self._MonticuloBinario__lista.extend(lista_de_tuplas) # Acceder a __lista del padre
        self._MonticuloBinario__tamanio = len(lista_de_tuplas) # Acceder a __tamanio del padre

        #empieza en el ultimo padre
        i = self._MonticuloBinario__tamanio // 2 # Acceder a __tamanio del padre
        while i > 0:
            self.infiltrarAbajo_prim(i)
            i -= 1

    def buscar_prim(self,elemento):
        if self.estaVacio():
            return "EL montículo está vacío"

        for tupla in self._MonticuloBinario__lista[1:]: # Acceder a __lista del padre
            if tupla[1] == elemento:
                return True
        return False

    def decrementarClave(self, elemento_a_actualizar, nueva_prioridad):
        if self.estaVacio():
            raise ValueError("El montículo está vacío. No se puede decrementar una clave.")

        indice = -1
        for i in range(1, self._MonticuloBinario__tamanio + 1): # Acceder a __tamanio del padre
            if self._MonticuloBinario__lista[i][1] == elemento_a_actualizar: # Acceder a __lista del padre
                indice = i
                break

        if indice == -1:
            raise ValueError(f"El elemento '{elemento_a_actualizar}' no se encontró en el montículo.")

        prioridad_actual = self._MonticuloBinario__lista[indice][0] # Acceder a __lista del padre

        self._MonticuloBinario__lista[indice] = (nueva_prioridad, elemento_a_actualizar) # Acceder a __lista del padre

        if self.__tipo == "min":
            if nueva_prioridad < prioridad_actual:
                self.infiltrarArriba_prim(indice)
            elif nueva_prioridad > prioridad_actual:
                self.infiltrarAbajo_prim(indice)

        elif self.__tipo == "max":
            if nueva_prioridad > prioridad_actual:
                self.infiltrarArriba_prim(indice)
            elif nueva_prioridad < prioridad_actual:
                self.infiltrarAbajo_prim(indice)
