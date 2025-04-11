from modules.NodoLDE import NodoLDE
class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
    
    @property
    def cabeza(self):
        return self.__cabeza

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
            return self
        else:
            dato.siguiente = self.__cabeza
            self.__cabeza = dato
            return self
    
    def agregar_al_final(self,item):

        """Agrega un elemento al final de la lista"""

        actual = self.__cabeza
        dato = NodoLDE(item)

        if actual is None:
            self.__cabeza = dato
            return self
        elif actual.siguiente is None:
            actual.siguiente = dato
            return self
        else:
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = dato
            return self
 
    def insertar(self,item,posicion):

        """Inserta un dato en una determinada posicion"""

        if posicion <0:
            raise ValueError("La posición debe ser mayor o igual a 0")
        elif posicion == 0:
            self.agregar_al_inicio(item)
            return self
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
                return self
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

    def concatenar(self,ListaDE):

        """Concatena una segunda ListaDobleEnlazada al final de la primera"""

        if isinstance(ListaDE,ListaDobleEnlazada): 
            actual = self.__cabeza
            cabeza_segunda = ListaDE.cabeza
            if actual is None:
                self.__cabeza = cabeza_segunda
                return self
            elif actual.siguiente is None:
                actual.siguiente = cabeza_segunda
                return self
            else:
                while actual.siguiente is not None:
                    actual = actual.siguiente
                actual.siguiente = cabeza_segunda
                return self
        else:
            raise TypeError("El parámetro debe ser un objeto ListaDobleEnlazada")


    def __add__(self,ListaDE):

        """Retorna una nueva lista concatenando la existente y una nueva"""

        if isinstance(ListaDE,ListaDobleEnlazada): 
            actual = self.__cabeza
            cabeza_segunda = ListaDE.cabeza
            if actual is None:
                self.__cabeza = cabeza_segunda
                return self
            elif actual.siguiente is None:
                actual.siguiente = cabeza_segunda
                return self
            else:
                while actual.siguiente is not None:
                    actual = actual.siguiente
                actual.siguiente = cabeza_segunda
                return self
        else:
            raise TypeError("El parámetro debe ser un objeto ListaDobleEnlazada")