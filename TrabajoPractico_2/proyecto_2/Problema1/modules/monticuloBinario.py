class MonticuloBinario:
    def __init__(self,tipo_de_monticulo):
        self.__lista = [None]
        self.__tamanio = 0
        if tipo_de_monticulo == "min" or tipo_de_monticulo == "max": 
            self.__tipo = tipo_de_monticulo.lower()
        else:
            raise ValueError("Debe ingresa por tipo, max o min")
    
    @property
    def tamanio(self): 
        return self.__tamanio
    
    def __iter__(self):
        return iter(self.__lista)
    

    def mostrar_monticulo(self):
        """
        Permite obtener la lista de nodos
        """

        if self.estaVacio():
            return 
        else:
            return self.__lista
    

    def insertar(self,clave):
        """
        Inserta un nuevo nodo
        """
        self.__lista.append(clave)
        self.__tamanio += 1
        self.infiltrarArriba(self.__tamanio)
        
    def infiltrarArriba(self,i):
        while i // 2 > 0:
            if (self.__tipo == "min" and self.__lista[i]<self.__lista[i//2]) or \
            (self.__tipo == "max" and self.__lista[i]>self.__lista[i//2]): 
                
                temp = self.__lista[i//2]
                self.__lista[i//2] = self.__lista[i]
                self.__lista[i] = temp
            
            else: 
                break

            i = i//2

    def infiltrarAbajo(self,i):
        while (i * 2) <= self.__tamanio:  
            hijo_menor = i * 2
            if (i * 2 + 1) <= self.__tamanio:  
                if (self.__tipo == "min" and self.__lista[i * 2 + 1] < self.__lista[hijo_menor]) or \
                (self.__tipo == "max" and self.__lista[i * 2 + 1] > self.__lista[hijo_menor]):
                        
                        hijo_menor = i * 2 + 1
                
            if (self.__tipo == "min" and self.__lista[i] > self.__lista[hijo_menor]) or \
            (self.__tipo == "max" and self.__lista[i] < self.__lista[hijo_menor]):
                    temp = self.__lista[i]
                    self.__lista[i] = self.__lista[hijo_menor]
                    self.__lista[hijo_menor] = temp
            else:
                    break 
            
            i = hijo_menor

    def eliminarRaiz(self):
        """
        Elimina la raíz y la reemplaza manteniendo la correcta estructura
        """
        raiz = self.__lista[1]
        self.__lista[1] = self.__lista[self.__tamanio]
        self.__tamanio -= 1
        self.__lista.pop()
        self.infiltrarAbajo(1)
        return raiz
        
        
    def buscarRaiz(self):
        """
        Devuelve la raíz del montículo
        """
        if self.estaVacio():
            return f"EL montículo está vacío"

        return self.__lista[1]
    
    def estaVacio(self):
        """
        Devuelve True o False según el monticulo tenga o no aunque sea un nodo
        """
        if self.__tamanio == 0:
            return True
        return False
    
    def construirMonticulo(self,lista):
        """
        Construye un monticulo a partir de una lista de elementos
        """
        for i in lista: 
            self.insertar(i)
        
    def buscar(self,clave):
        """
        Devuelve True o False según se encuentre la clave en el montículo
        """
        if self.estaVacio():
            return f"EL montículo está vacío"

        for i in self.__lista:
            if i == clave:
                return True
        else:
            return False