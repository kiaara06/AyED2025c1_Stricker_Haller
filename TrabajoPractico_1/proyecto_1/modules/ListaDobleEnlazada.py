from modules.NodoLDE import NodoLDE
class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None

    def estaVacia(self):

        """Verifica si la lista tiene elementos"""

        vacia = False
        if self.__cabeza is None:
            vacia = True
        return vacia
    
    def __len__(self):

        """Devuelve el tamaño de la lista"""

        actual = self.__cabeza
        contador = 0
        while actual is not None:
            contador = contador +1
            actual = actual.siguiente
        if contador == 0:
            return "La lista está vacia"
        else:
            return contador
    
    def agregar_al_inicio(self,item):

        """Agrega un elemento al principio de la lista"""

        dato = NodoLDE(item)
        if self.__cabeza is None:
            self.__cabeza = dato
        else:
            dato.siguiente = self.__cabeza
            self.__cabeza = dato
    
    def agregar_al_final(self,item):

        """Agrega un elemento al final de la lista"""

        actual = self.__cabeza
        dato = NodoLDE(item)

        if actual is None:
            self.__cabeza = dato
        elif actual.siguiente is None:
            actual.siguiente = dato
        else:
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = dato
 
    def insertar(self,item,posicion):

        """Inserta un dato en una determinada posicion"""

        if posicion <0:
            raise ValueError("La posición debe ser mayor o igual a 0")
        elif posicion == 0:
            self.agregar_al_inicio(item)
        else:
            dato = NodoLDE(item)
            actual = self.__cabeza
            previo = None
            contador = 0
            while actual is not None and contador != posicion:
                previo = actual
                actual = actual.siguiente
                contador = contador+1
            if contador == posicion:
                dato.anterior = previo
                dato.siguiente = actual
            elif actual is None:
                if previo is None:
                    raise ValueError("La lista está vacia. No existe la posicion pedida")
                else:
                    dato.anterior = previo
                    return "La posicion no existe. Se agregó al final de la lista"

    def extraer(self,posicion):
        
        """Retorna el item ubicado en dicha posicion"""

        if posicion <0:
            raise ValueError("La posicion debe ser mayor o igual a 0")
        else: 
            actual = self.__cabeza
            previo = None
            contador = 0
            if actual is None:
                return "La lista está vacia"
            elif contador == posicion:
                    item = actual.dato
                    self.__cabeza = actual.siguiente
                    return item
            else:
                encontrado = False
                while actual is not None and not encontrado:
                    if contador == posicion:
                        encontrado = True
                    else:
                        previo = actual
                        actual = actual.siguiente
                        contador = contador +1
                if encontrado:
                    item = actual.dato
                    previo.siguiente = actual.siguiente
                    return item
                else:
                    item = previo.dato
                    previo.anterior.siguiente = None
                    return item
    
    def copiar(self):
        
        """Crea otro objeto ListaDobleEnlazada igual al existente"""

        actual = self.__cabeza
        lista_copia = ListaDobleEnlazada()

        while actual is not None:
            nuevo_actual = actual.dato
            lista_copia.agregar_al_final(nuevo_actual)
            actual = actual.siguiente
        
        return lista_copia

    def invertir(self):
        
        """Invierte el orden de los elementos de la lista"""

        actual = self.__cabeza
        previo = None
        if actual is None:
            return "La lista está vacia"
        else:
            while actual is not None:
                siguiente = actual.siguiente
                actual.siguiente = previo
                previo = actual
                actual = siguiente
            self.__cabeza = previo
            return self



    def remover(self,item):

        """Remueve un dato de la lista, pero no lo devuelve"""

        actual = self.__cabeza
        previo = None
        encontrado = False
        while actual is not None and not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.siguiente
        if encontrado:
            if actual is self.__cabeza and previo is None:
                self.__cabeza = actual.siguiente
            else:
                previo.siguiente=actual.siguiente
            return "Se removió el item"
        
        else:
            if actual is None and previo is None:
                return "La lista esta vacia"
            else: 
                return "El item no se encuentra en la lista"




    def buscar(self,item):

        """Indica si un item se encuentra en la lista"""

        actual = self.__cabeza
        encontrado = False
        while actual is not None and not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                actual = actual.siguiente

        return encontrado
    


    def iterar(self):

        """Devuelve una lista de python con los items de la lista"""
        actual = self.__cabeza
        if actual is None:
            return "La lista está vacia"
        else:
            items = [] 
            while actual is not None:
                items.append(actual.dato)
                actual = actual.siguiente
            return items

    
    def indice(self,item):

        "Devuelve la posicion del item en la lista"

        actual = self.__cabeza
        indice = 0
        if actual is None:
            return "La lista está vacia"
        elif actual.dato == item:
                return indice
        else:
            encontrado = False
            while actual is not None and not encontrado:
                if actual.dato == item:
                    encontrado = True
                else:
                    actual = actual.siguiente
                    indice = indice +1
            if encontrado:
                return indice
            else:
                return "El item no está en la lista"
            
    
            
    def extraer(self,item):

        "Remueve un determiando dato de la lista y lo devuelve"

        actual = self.__cabeza
        previo = None
        encontrado = False
        while actual is not None and not encontrado:
            if actual.dato == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.siguiente
        if encontrado:
            dato = actual
            if actual is self.__cabeza and previo is None:
                self.__cabeza = actual.siguiente
            else:
                previo.siguiente= actual.siguiente
            return actual
        
        else:
            if actual is None and previo is None:
                return "La lista esta vacia"
            else: 
                return "El item no se encuentra en la lista"
        

        
        return lista_copia

    def cola(self):

        """Retorna el útlimo item de la lista"""

        if self.estaVacia() is not True:
            posicion = self.tamaño() -1
            ultimo_dato = self.obtenerItem(posicion)
            return ultimo_dato
        else:
            return "La lista está vacia"

    
            
    def ordenarMayorMenor(self):

        """Ordena la lista de mayor a menor"""

        actual = self.__cabeza
        if actual is None:
            return "La lista esta vacia"
        else:
            lista_elementos = []
            while actual is not None:
                item = actual.dato
                lista_elementos.append(item)
                self.remover(item)
                actual = actual.siguiente
            lista_invertida = sorted(lista_elementos,reverse=True)
            for e in lista_invertida:
                self.anexar(e)
            return self

l = ListaDobleEnlazada()
l.agregar_al_final(55)
l.agregar_al_final(58)
l.agregar_al_final(66)
print(l.iterar())