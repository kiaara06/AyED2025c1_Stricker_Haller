from modules.monticuloBinario import MonticuloBinario
   
class ColaDePrioridad:
    def __init__(self):
        self.__cola = MonticuloBinario("min")

    @property
    def cola(self):
        return self.__cola

    def ingresar(self,dato):
        self.__cola.insertar(dato)
    
    def avanzar(self):
        dato_eliminado = self.__cola.eliminarRaiz()
        return dato_eliminado
    
    def __len__(self):
        return self.__cola.tamanio
    
    def __iter__(self):
        return iter(self.__cola)

if __name__ == "__main__":
    c = ColaDePrioridad()
    c.ingresar(5)
    c.ingresar(5)
    c.ingresar(1)
    c.ingresar(5)
    print(c.cola.mostrar_monticulo())
    eliminado = c.avanzar()
    print(eliminado)
    print(c.cola.mostrar_monticulo())
    for i in c:
        print(i)