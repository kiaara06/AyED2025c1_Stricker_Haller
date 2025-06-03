from modules.monticuloBinario import MonticuloBinario

class MonticuloBinarioPrim(MonticuloBinario):
    def __init__(self):
        super().__init__()
    
    def insertar_prim(self,tupla_clave_y_elemento): #cambio necesario (self,clave) a (self,tupla)

        """Inserta un nuevo nodo"""

        if self.__tipo == "min": 
            self.__lista.append(tupla_clave_y_elemento)
            self.__tamanio += 1
            self.infiltrarArriba_prim(self.__tamanio)
        
        elif self.__tipo == "max": 
            self.__lista.append(tupla_clave_y_elemento)
            self.__tamanio += 1
            self.infiltrarArriba_prim(self.__tamanio)
    
    def infiltrarArriba_prim(self,i):
        while i // 2 > 0:
            if self.__tipo == "min":
                #Se cambió if self.__lista[i] < self.__lista[i//2]:
                #Por if self.__lista[i][0] < self.__lista[i//2][0]:
                if self.__lista[i][0]<self.__lista[i//2][0]:
                    temp = self.__lista[i//2]
                    self.__lista[i//2] = self.__lista[i]
                    self.__lista[i] = temp
                i = i//2
            elif self.__tipo == "max":
                #Se cambió if self.__lista[i] > self.__lista[i//2]:
                #Por if self.__lista[i][0] > self.__lista[i//2][0]:
                if self.__lista[i][0]>self.__lista[i//2][0]:
                    temp = self.__lista[i//2]
                    self.__lista[i//2] = self.__lista[i]
                    self.__lista[i] = temp
                i = i//2

    def infiltrarAbajo_prim(self,i):
        while (i * 2) <= self.__tamanio:  
            hijo_menor = i * 2
            if (i * 2 + 1) <= self.__tamanio:  
                if self.__tipo == "min":
                #Se cambió if self.__lista[i * 2 + 1] < self.__lista[hijo_menor]:
                #Por if self.__lista[i * 2 + 1][0] < self.__lista[hijo_menor][0]:
                    if self.__lista[i * 2 + 1][0] < self.__lista[hijo_menor][0]:
                        hijo_menor = i * 2 + 1
                elif self.__tipo == "max":
                    if self.__lista[i * 2 + 1][0] > self.__lista[hijo_menor][0]:
                        hijo_menor = i * 2 + 1

            if self.__tipo == "min":
                #Se cambió if self.__lista[i] > self.__lista[hijo_menor]:
                #Por if self.__lista[i][0] > self.__lista[hijo_menor][0]:
                if self.__lista[i][0] > self.__lista[hijo_menor][0]:
                    temp = self.__lista[i]
                    self.__lista[i] = self.__lista[hijo_menor]
                    self.__lista[hijo_menor] = temp
                else:
                    break 
            elif self.__tipo == "max":
                #Se cambió if self.__lista[i] < self.__lista[hijo_menor][0]:
                #Por if self.__lista[i][0] < self.__lista[hijo_menor][0]:
                if self.__lista[i][0] < self.__lista[hijo_menor][0]:
                    temp = self.__lista[i]
                    self.__lista[i] = self.__lista[hijo_menor]
                    self.__lista[hijo_menor] = temp
                else:
                    break
            i = hijo_menor
    
    def construirMonticulo_prim(self,lista_de_tuplas): 
        """
        Construye un montículo a partir de una lista de elementos (prioridad, item).
        Utiliza el algoritmo de heapify para construir el montículo de forma eficiente.
        """
        self.__lista = [None] #resetea para arrancar de cero
        self.__lista.extend(lista_de_tuplas) 
        self.__tamanio = len(lista_de_tuplas)

        #empieza en el ultimo padre
        i = self.__tamanio // 2
        while i > 0:
            self.infiltrarAbajo_prim(i)
            i -= 1
    
    def buscar_prim(self,elemento):
        if self.estaVacio():
            return "EL montículo está vacío"

        for item_tuple in self.__lista[1:]:
            if item_tuple[1] == elemento: 
                return True
        return False

    def decrementarClave(self, elemento_a_actualizar, nueva_prioridad):
        if self.estaVacio():
            raise ValueError("El montículo está vacío. No se puede decrementar una clave.")

        indice = -1
        for i in range(1, self.__tamanio + 1):
            if self.__lista[i][1] == elemento_a_actualizar:
                indice = i
                break

        if indice == -1:
            raise ValueError(f"El elemento '{elemento_a_actualizar}' no se encontró en el montículo.")

        prioridad_actual = self.__lista[indice][0]

        self.__lista[indice] = (nueva_prioridad, elemento_a_actualizar)

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