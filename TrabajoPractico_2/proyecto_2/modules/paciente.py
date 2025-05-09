
from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self,llegada):
        n = len(nombres)
        self.__llegada = llegada
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def llegada(self):
        return self.__llegada
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def riesgo(self):
        return self.__riesgo
    
    @property
    def descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad

    def __lt__(self,otro_dato):
        if self.riesgo < otro_dato.riesgo :
            return True
        elif self.riesgo == otro_dato.riesgo:
            if self.llegada < otro_dato.llegada:
                return True
            else:
                return False
        else:
            return False
        

if __name__ == "__main__":
    p1 = Paciente(1)
    p2 = Paciente(2)
    print(p1.riesgo,p2.riesgo)
    if p1<p2:
        print("funciona")
#lista_pacientes = []   
#for i in range(4):     
    #h = Paciente()
    #lista_pacientes.append(h)

#for paciente in lista_pacientes:
    #print(str(paciente))
        