class NodoArbolAVL:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0
    
    @property
    def padre(self):
        return self.__padre
    @padre.setter
    def padre(self, nuevo_padre):
        self.__padre = nuevo_padre
    
    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo
    @hijoIzquierdo.setter
    def hijoIzquierdo(self,nuevo_hizq):
        self.__hijoIzquierdo = nuevo_hizq
        
    @property
    def hijoDerecho(self):
        return self.__hijoDerecho
    @hijoDerecho.setter
    def hijoDerecho(self,nuevo_hder):
        self.__hijoDerecho = nuevo_hder
    
    @property
    def clave(self):
        return self.__clave
    @clave.setter
    def clave(self, nueva_clave):
        self.__clave = nueva_clave
    
    @property
    def cargaUtil(self):
        return self.__cargaUtil
    @cargaUtil.setter
    def cargaUtil(self, nueva_carga_util):
        self.__cargaUtil = nueva_carga_util
    
    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio
    @factorEquilibrio.setter
    def factorEquilibrio(self, nuevo_factor):
        self.__factorEquilibrio = nuevo_factor

    def tieneHijoIzquierdo(self):
        """
        Devuelve True o False si tiene o no un hijo izquierdo.
        """
        return self.hijoIzquierdo is not None

    def tieneHijoDerecho(self):
        """
        Devuelve True o False si tiene o no un hijo derecho.
        """
        return self.hijoDerecho is not None

    def esHijoIzquierdo(self):
        """Devuelve True o False si es o no un hijo izquierdo"""
        return self.padre is not None and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        """
        Devuelve True o False si es o no un hijo derecho.
        """
        return self.padre is not None and self.padre.hijoDerecho == self

    def esRaiz(self):
        """
        Devuelve True o False si es la raiz del AVL.
        """
        return self.padre is None

    def esHoja(self):
        """
        Devuelve True si no tiene o no hijos.
        """
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        """
        Devuelve True si tiene aunque sea un hijo.
        """
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        """
        Devuelve True si tiene los dos hijos.
        """
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        """
        Reemplaza algun dato.
        """
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        """
        Devuelve el número de nodos en el árbol.
        """
        return self.tamano

    def __len__(self):
        """
        Permite usar len(arbol_avl) para obtener el tamaño.
        """
        return self.tamano

    def _altura(self, nodo):
        """
        Devuelve la altura del nodo.
        """
        if nodo is None:
            return -1
        return 1 + max(self._altura(nodo.hijoIzquierdo), self._altura(nodo.hijoDerecho))

    def _actualizarEquilibrio(self, nodo):
        """
        Actualiza el factor de equlibrio de un nodo.
        """
        if nodo is None:
            return
        altura_izq = self._altura(nodo.hijoIzquierdo)
        altura_der = self._altura(nodo.hijoDerecho)
        nodo.factorEquilibrio = altura_izq - altura_der

    def _rotarIzquierda(self, rotRaiz):
        """
        Hace una rotacion simple a la izquierda cuando el árbol se
        desequilibra hacia la derecha.
        """
        nuevaRaiz = rotRaiz.hijoDerecho
        
        rotRaiz.hijoDerecho = nuevaRaiz.hijoIzquierdo
        if nuevaRaiz.hijoIzquierdo is not None:
            nuevaRaiz.hijoIzquierdo.padre = rotRaiz

        nuevaRaiz.hijoIzquierdo = rotRaiz
        rotRaiz.padre = nuevaRaiz

        self._actualizarEquilibrio(rotRaiz)
        self._actualizarEquilibrio(nuevaRaiz)
        
        return nuevaRaiz
    
    def _rotarDerecha(self, rotRaiz):
        """
        Hace una rotacion simple a la derecha cuando el árbol se
        desequilibra hacia la izquierda.
        """
        nuevaRaiz = rotRaiz.hijoIzquierdo
        
        rotRaiz.hijoIzquierdo = nuevaRaiz.hijoDerecho
        if nuevaRaiz.hijoDerecho is not None:
            nuevaRaiz.hijoDerecho.padre = rotRaiz

        nuevaRaiz.hijoDerecho = rotRaiz
        rotRaiz.padre = nuevaRaiz

        self._actualizarEquilibrio(rotRaiz)
        self._actualizarEquilibrio(nuevaRaiz)

        return nuevaRaiz 

    def _reequilibrar(self, nodo):
        """
        Reequilibra el nodo dado si su factor de equilibrio indica un desequilibrio.
        Aplica las rotaciones necesarias (simples o dobles).
        """
        if nodo.factorEquilibrio < -1: #desequilibrio a la derecha
            if nodo.hijoDerecho.factorEquilibrio > 0: #caso derecha-izquierda
                nodo.hijoDerecho = self._rotarDerecha(nodo.hijoDerecho)
            return self._rotarIzquierda(nodo) #derecha-derecha o #derecha-izquierda
        
        elif nodo.factorEquilibrio > 1: #desequilibrio a la izquierda
            if nodo.hijoIzquierdo.factorEquilibrio < 0: #caso izquierda-derecha
                nodo.hijoIzquierdo = self._rotarIzquierda(nodo.hijoIzquierdo)
            return self._rotarDerecha(nodo) #izquierda-izquiera o izquierda-derecha
        
        return nodo

    def agregar(self, clave, valor):
        """
        Agrega un nodo al avl, haciendo uso de otro 
        método recursivo que se encarga de ubicarlo adecuadamente.
        """
        if self.raiz:
            self.raiz = self._agregar(clave, valor, self.raiz)
            self.raiz.padre = None
        else:
            self.raiz = NodoArbolAVL(clave, valor)
        self.tamano += 1

    def _agregar(self, clave, valor, nodoActual):
        """
        Método recursivo que se encarga de posicionar adecuadamente el 
        nuevo nodo,y asegurar el equilibrio del avl
        """
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                nodoActual.hijoIzquierdo = self._agregar(clave, valor, nodoActual.hijoIzquierdo)
                nodoActual.hijoIzquierdo.padre = nodoActual
            else:
                nodoActual.hijoIzquierdo = NodoArbolAVL(clave, valor, padre=nodoActual)

        elif clave > nodoActual.clave:
            if nodoActual.tieneHijoDerecho():
                nodoActual.hijoDerecho = self._agregar(clave, valor, nodoActual.hijoDerecho)
                nodoActual.hijoDerecho.padre = nodoActual
            else:
                nodoActual.hijoDerecho = NodoArbolAVL(clave, valor, padre=nodoActual)

        else:
            nodoActual.cargaUtil = valor
            return nodoActual

        self._actualizarEquilibrio(nodoActual)

        if nodoActual.factorEquilibrio > 1 or nodoActual.factorEquilibrio < -1:
            return self._reequilibrar(nodoActual)
        
        return nodoActual

    def __setitem__(self,c,v):
       """
       Permite usar arbol[clave] = valor para agregar.
       """
       self.agregar(c,v)

    def _obtener(self,clave,nodoActual):
        """
        Función auxiliar recursiva para obtener un nodo por clave.
        """
        if not nodoActual:
            return None
        elif nodoActual.clave == clave:
            return nodoActual
        elif clave < nodoActual.clave:
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else:
            return self._obtener(clave,nodoActual.hijoDerecho)
       
    def obtener(self,clave):
        """
        Obtiene la carga útil asociada a una clave.
        """
        if self.raiz:
           res = self._obtener(clave,self.raiz)
           if res:
                   return res.cargaUtil
           else:
                   return None
        else:
           return None

    def __getitem__(self,clave):
       """
       Permite usar arbol[clave] para obtener la carga útil.
       """
       return self.obtener(clave)

    def __contains__(self,clave):
       """
       Permite usar 'clave in arbol' para verificar existencia.
       """
       if self._obtener(clave,self.raiz):
           return True
       else:
           return False
    
    def _encontrarMin(self, nodo):
      """
      Encuentra el nodo con la clave mínima en un subárbol dado.
      """
      actual = nodo
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual
    
    def _encontrarSucesor(self, nodo):
      """
      Encuentra el sucesor in-order de un nodo dado.
      """
      suc = None
      if nodo.tieneHijoDerecho():
          suc = self._encontrarMin(nodo.hijoDerecho)
      else:
          actual = nodo
          while actual.padre and actual.esHijoDerecho():
              actual = actual.padre
          suc = actual.padre 
      return suc

    def _remover(self,clave, nodoActual):
        """
        Elimina un nodo del árbol y maneja la actualización del factor de equilibrio.
        Este método es llamado internamente por 'eliminar'.
        """
        if not nodoActual:
            return nodoActual

        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                nodoActual.hijoIzquierdo = self._remover(clave, nodoActual.hijoIzquierdo)
                if nodoActual.hijoIzquierdo:
                    nodoActual.hijoIzquierdo.padre = nodoActual
            else:
                return nodoActual
        elif clave > nodoActual.clave:
            if nodoActual.tieneHijoDerecho():
                nodoActual.hijoDerecho = self._remover(clave, nodoActual.hijoDerecho)
                if nodoActual.hijoDerecho:
                    nodoActual.hijoDerecho.padre = nodoActual
            else:
                return nodoActual
        else:
            if nodoActual.esHoja():
                return None
            elif nodoActual.tieneAmbosHijos():
                sucesor = self._encontrarMin(nodoActual.hijoDerecho)
                nodoActual.clave = sucesor.clave
                nodoActual.cargaUtil = sucesor.cargaUtil
                nodoActual.hijoDerecho = self._remover(sucesor.clave, nodoActual.hijoDerecho)
                if nodoActual.hijoDerecho:
                    nodoActual.hijoDerecho.padre = nodoActual
            else:
                if nodoActual.tieneHijoIzquierdo():
                    hijo_que_sube = nodoActual.hijoIzquierdo
                else:
                    hijo_que_sube = nodoActual.hijoDerecho
                hijo_que_sube.padre = nodoActual.padre
                return hijo_que_sube
        
        self._actualizarEquilibrio(nodoActual)
        return self._reequilibrar(nodoActual)

    def eliminar(self,clave):
        """
        Elimina un nodo del árbol por su clave.
        """
        if self.raiz:
            nueva_raiz_o_none = self._remover(clave, self.raiz)
            
            if nueva_raiz_o_none is None:
                if self.tamano == 1 and self.raiz.clave == clave:
                    self.raiz = None
                    self.tamano = 0
                else:
                    raise KeyError('Error, la clave no está en el árbol o ya fue eliminada.')
            else:
                self.raiz = nueva_raiz_o_none
                self.raiz.padre = None
                self.tamano -= 1
                
        else:
            raise KeyError('Error, el árbol está vacío o la clave no está en el árbol.')

    def __delitem__(self,clave):
       """
       Permite usar del arbol[clave] para eliminar.
       """
       self.eliminar(clave)

    def _encontrar_min_max_rango(self, nodoActual, clave1, clave2, min_valor=float('inf'), max_valor=float('-inf')):
        """
        Encuentra los valores mínimo y máximo de carga útil dentro de un rango de claves.
        Realiza un recorrido recursivo dentro del rango.
        """
        if not nodoActual:
            return min_valor, max_valor
        
        if clave1 <= nodoActual.clave <= clave2:
            min_valor = min(min_valor, nodoActual.cargaUtil)
            max_valor = max(max_valor, nodoActual.cargaUtil)

        if clave1 < nodoActual.clave:
            min_valor, max_valor = self._encontrar_min_max_rango(nodoActual.hijoIzquierdo, clave1, clave2, min_valor, max_valor)

        if clave2 > nodoActual.clave:
            min_valor, max_valor = self._encontrar_min_max_rango(nodoActual.hijoDerecho, clave1, clave2, min_valor, max_valor)

        return min_valor, max_valor
    
    def encontrar_min_max_rango(self, clave1, clave2):
        """
        Devuelve el valor mínimo y máximo de carga útil en el árbol
        para claves dentro del rango [clave1, clave2].
        """
        if self.raiz is None:
            return None, None
        else:
            min_valor, max_valor = self._encontrar_min_max_rango(self.raiz, clave1, clave2)
            if min_valor == float('inf') and max_valor == float('-inf'):
                return None, None 
            return min_valor, max_valor

    def _recolectar_valores_rango(self, nodoActual, clave1, clave2, lista_valores):
        """
        Recolecta la clave y su valor correspondiente en un rango de nodos.
        Realiza un recorrido in-order dentro del rango para asegurar el orden.
        """
        if not nodoActual:
            return
        
        if clave1 < nodoActual.clave:
            self._recolectar_valores_rango(nodoActual.hijoIzquierdo, clave1, clave2, lista_valores)

        if clave1 <= nodoActual.clave <= clave2:
            lista_valores.append([nodoActual.clave, nodoActual.cargaUtil])

        if clave2 > nodoActual.clave:
            self._recolectar_valores_rango(nodoActual.hijoDerecho, clave1, clave2, lista_valores)

    def devolver_valores_rango(self, clave1, clave2):
        """
        Devuelve una lista de pares [clave, valor] para los nodos
        cuyas claves están dentro del rango [clave1, clave2].
        """
        lista_valores = []
        self._recolectar_valores_rango(self.raiz, clave1, clave2, lista_valores)
        return lista_valores

if __name__=="__main__":
    a = ArbolAVL()
    a.agregar(1,1)
    a.agregar(2,2)
    a.agregar(3,3)

    print(a.raiz.cargaUtil)
