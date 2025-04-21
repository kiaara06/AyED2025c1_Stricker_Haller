from modules.NodoLDE import NodoLDE

class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0

    @property
    def cabeza(self):
        return self.__cabeza
    @property
    def cola(self):
        return self.__cola
    @property
    def tamanio(self):
        return self.__tamanio

    def estaVacia(self):
        """Verifica si la lista tiene elementos"""
        return self.__cabeza is None

    def __len__(self):
        """Devuelve el tamaño de la lista"""
        return self.__tamanio

    def agregar_al_inicio(self, item):
        """Agrega un elemento al principio de la lista"""
        nuevo_nodo = NodoLDE(item)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = None
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, item):
        """Agrega un elemento al final de la lista"""
        nuevo_nodo = NodoLDE(item)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__cola
            self.__cola.siguiente = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

    def insertar(self, item, posicion):
        """Inserta un dato en una determinada posicion"""
        if posicion < 0:
            raise IndexError("La posición está fuera de rango")
        elif posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion >= self.__tamanio:
            self.agregar_al_final(item)
        else:
            nuevo_nodo = NodoLDE(item)
            actual = self.__cabeza
            contador = 0
            while contador < posicion - 1:
                actual = actual.siguiente
                contador += 1
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            self.__tamanio += 1

    def extraer(self, posicion=None):
        """Retorna el item ubicado en dicha posicion"""
            
        if posicion == None: 
            if self.__cola is None:
                raise IndexError("La lista está vacía")
            item = self.__cola.dato
            self.__cola = self.__cola.anterior
            if self.__cola is not None:
                self.__cola.siguiente = None
            else:
                self.__cabeza = None
            self.__tamanio -= 1
            return item
        
        elif posicion < 0:
            posicion = self.__tamanio + posicion
            if posicion < 0:
                raise IndexError("La posición está fuera de rango")
            elif posicion == 0:
                if self.__cabeza is None:
                    raise IndexError("La lista está vacía")
                item = self.__cabeza.dato
                self.__cabeza = self.__cabeza.siguiente
                if self.__cabeza is not None:
                    self.__cabeza.anterior = None
                else:
                    self.__cola = None
                self.__tamanio -= 1
                return item
            elif posicion >= (self.__tamanio - 1):
                if self.__cola is None:
                    raise IndexError("La lista está vacía")
                item = self.__cola.dato
                self.__cola = self.__cola.anterior
                if self.__cola is not None:
                    self.__cola.siguiente = None
                else:
                    self.__cabeza = None
                self.__tamanio -= 1
                return item
            else: 
                actual = self.__cabeza
                contador = 0
                while contador < posicion:
                    actual = actual.siguiente
                    contador += 1
                    
                item = actual.dato
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                self.__tamanio -= 1
                return item
        else:
            if posicion == 0:
                if self.__cabeza is None:
                    raise IndexError("La lista está vacía")
                item = self.__cabeza.dato
                self.__cabeza = self.__cabeza.siguiente
                if self.__cabeza is not None:
                    self.__cabeza.anterior = None
                else:
                    self.__cola = None
                self.__tamanio -= 1
                return item
            elif posicion >= (self.__tamanio - 1):
                if self.__cola is None:
                    raise IndexError("La lista está vacía")
                item = self.__cola.dato
                self.__cola = self.__cola.anterior
                if self.__cola is not None:
                    self.__cola.siguiente = None
                else:
                    self.__cabeza = None
                self.__tamanio -= 1
                return item
            else: 
                actual = self.__cabeza
                contador = 0
                while contador < posicion:
                    actual = actual.siguiente
                    contador += 1
                item = actual.dato
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                self.__tamanio -= 1
                return item


    def copiar(self):
        """Crea otro objeto ListaDobleEnlazada igual al existente"""
        lista_copia = ListaDobleEnlazada()
        actual = self.__cabeza
        while actual is not None:
            lista_copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_copia

    def invertir(self):
        """Invierte el orden de los elementos de la lista"""
        if self.__tamanio <= 1:
            return self
        actual = self.__cabeza
        self.__cabeza, self.__cola = self.__cola, self.__cabeza
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
        return self

    def concatenar(self, ListaDE):

        """Concatena una segunda ListaDobleEnlazada al final de la primera"""

        if not isinstance(ListaDE, ListaDobleEnlazada):
            raise TypeError("El parámetro debe ser un objeto ListaDobleEnlazada")
        if ListaDE.estaVacia():
            return self
        if self.estaVacia():
            self.__cabeza = ListaDE.__cabeza
            self.__cola = ListaDE.__cola
        else:
            self.__cola.siguiente = ListaDE.__cabeza
            self.__cola = ListaDE.__cola
        self.__tamanio += len(ListaDE)
        return self

    def __add__(self, otra_lista):
        """Retorna una nueva lista concatenando la existente y una nueva"""
        if not isinstance(otra_lista, ListaDobleEnlazada):
            raise TypeError("El parámetro debe ser un objeto ListaDobleEnlazada")
        nueva_lista = self.copiar()
        nueva_lista.concatenar(otra_lista)
        return nueva_lista

    def __iter__(self):
            """Permite iterar sobre los elementos de la lista """
            elementos = []
            actual = self.__cabeza
            while actual is not None:
                elementos.append(actual.dato)
                actual = actual.siguiente
            return iter(elementos)
