class MonticuloBinario:
    def __init__(self,tipo_de_monticulo):
        self.__lista = [None]
        self.__tamanio = 0
        if tipo_de_monticulo == "min" or tipo_de_monticulo == "max": 
            self.__tipo = tipo_de_monticulo.lower()
        else:
            raise ValueError("Debe ingresa por tipo, maxima o minimo")
    
    @property
    def tamanio(self): 
        return self.__tamanio
    

    def mostrar_monticulo(self):
        if self.tamanio == 0:
            return 
        else:
            return self.__lista
    

    def insertar(self,clave):
        if self.__tipo == "min": 
            self.__lista.append(clave)
            self.__tamanio += 1
            self.infiltrarArriba(self.__tamanio)
        
        elif self.__tipo == "max": 
            self.__lista.append(clave)
            self.__tamanio += 1
            self.infiltrarArriba(self.__tamanio)

    
    def infiltrarArriba(self,i):
        while i // 2 > 0:
            if self.__tipo == "min":
                if self.__lista[i]<self.__lista[i//2]:
                    temp = self.__lista[i//2]
                    self.__lista[i//2] = self.__lista[i]
                    self.__lista[i] = temp
                i = i//2
            elif self.__tipo == "max":
                if self.__lista[i]>self.__lista[i//2]:
                    temp = self.__lista[i//2]
                    self.__lista[i//2] = self.__lista[i]
                    self.__lista[i] = temp
                i = i//2

    def infiltrarAbajo(self,i):
        while (i * 2) <= self.__tamanio:  
            hijo_menor = i * 2
            if (i * 2 + 1) <= self.__tamanio:  
                if self.__tipo == "min":
                    if self.__lista[i * 2 + 1] < self.__lista[hijo_menor]:
                        hijo_menor = i * 2 + 1
                elif self.__tipo == "max":
                    if self.__lista[i * 2 + 1] > self.__lista[hijo_menor]:
                        hijo_menor = i * 2 + 1

            if self.__tipo == "min":
                if self.__lista[i] > self.__lista[hijo_menor]:
                    temp = self.__lista[i]
                    self.__lista[i] = self.__lista[hijo_menor]
                    self.__lista[hijo_menor] = temp
                else:
                    break 
            elif self.__tipo == "max":
                if self.__lista[i] < self.__lista[hijo_menor]:
                    temp = self.__lista[i]
                    self.__lista[i] = self.__lista[hijo_menor]
                    self.__lista[hijo_menor] = temp
                else:
                    break
            i = hijo_menor

    def eliminarRaiz(self):
        if self.__tipo.lower() == "min":
            raiz = self.__lista[1]
            self.__lista[1] = self.__lista[self.__tamanio]
            self.__tamanio -= 1
            self.__lista.pop()
            self.infiltrarAbajo(1)
            return raiz
        if self.__tipo.lower() == "max":
            raiz = self.__lista[1]
            self.__lista[1] = self.__lista[self.__tamanio]
            self.__tamanio -= 1
            self.__lista.pop()
            self.infiltrarAbajo(1)
            return raiz
