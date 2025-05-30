from modules.AVL import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        self.__mediciones = ArbolAVL()
    
    def guardar_temperatura(self,temperatura,fecha):
        """
        Guarda la medida de temperatura asociada a la fecha.
        """

        from datetime import datetime
        if not isinstance (temperatura,(int,float)):
            raise TypeError("La temperatura debe ser un float, o un int")
        else:
            if isinstance (temperatura,int):
                temperatura = float(temperatura)
            temp = temperatura
        
        if not isinstance (fecha,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f = datetime.strptime(fecha, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")

        if f and temp:
            self.__mediciones.agregar(f,temp)

    def devolver_temperatura(self,fecha): 
        """
        Devuelve la medida de temperatura en la fecha determinada.
        """
        from datetime import datetime
        if not isinstance (fecha,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f = datetime.strptime(fecha, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
        
        return self.__mediciones[f]

    def max_temp_rango(self,fecha1,fecha2):
        """
        Devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
        Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        """
        from datetime import datetime
        if not isinstance (fecha1,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f1 = datetime.strptime(fecha1, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")

        if not isinstance (fecha2,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f2 = datetime.strptime(fecha2, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
            
        if f1 and f2:
            temp_min, temp_max = self.__mediciones.encontrar_min_max_rango(f1,f2)
            return f"""La temperatura máxima registrada entre los rangos {f1} y {f2} es de {temp_max}°C"""


    def min_temp_rango(self,fecha1, fecha2): 
        """
        Devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). 
        Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        """

        from datetime import datetime
        if not isinstance (fecha1,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f1 = datetime.strptime(fecha1, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")

        if not isinstance (fecha2,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f2 = datetime.strptime(fecha2, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
            
        if f1 and f2:
            temp_min, temp_max = self.__mediciones.encontrar_min_max_rango(f1,f2)
            return f"""La temperatura mínima registrada entre los rangos {f1} y {f2} es de {temp_min}°C"""

    def temp_extremos_rango(self,fecha1,fecha2): 
        """
        Devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive 
        (fecha1 < fecha2).
        """
        from datetime import datetime
        if not isinstance (fecha1,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f1 = datetime.strptime(fecha1, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")

        if not isinstance (fecha2,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f2 = datetime.strptime(fecha2, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
            
        if f1 and f2:
            temp_min, temp_max = self.__mediciones.encontrar_min_max_rango(f1,f2)
            return f"""Las temperaturas máx y min registradas entre los rangos {f1} y {f2} son:
            La máxima: {temp_max}°C
            La mínima: {temp_min}°C"""


    def borrar_temperatura(self,fecha): 
        """
        Recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        """
        from datetime import datetime
        if not isinstance (fecha,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f = datetime.strptime(fecha, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
        
        del self.__mediciones[f] 
        return f"Se eliminó la temperatura registrada en la fecha {f}"


    def devolver_temperaturas(self,fecha1,fecha2):
        """
        devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el 
        formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        """
        from datetime import datetime
        if not isinstance (fecha1,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f1 = datetime.strptime(fecha1, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")

        if not isinstance (fecha2,str):
            raise TypeError("La fecha debe ser un string en formato dd/mm/aaaa")
        else:
            try: 
                f2 = datetime.strptime(fecha2, '%d/%m/%Y')
            except ValueError:
                raise ValueError("Formato de fecha incorrecto. Debe ser 'dd/mm/aaaa'")
            
        if f1 and f2:
            listado = []
            lista_mediciones = self.__mediciones.devolver_valores_rango(f1,f2)
            lista_mediciones = sorted(lista_mediciones, key = lambda item:item[0])

            for medicion in lista_mediciones:
                fecha = medicion[0]
                temp = medicion[1]
                listado.append(f"{fecha.strftime('%d/%m/%Y')} : {temp}°C")
            
            return listado


    def cantidad_muestras(self): 
        """
        devuelve la cantidad de muestras de la BD.
        """
        return f"La cantidad de muestras registradas es de: {len(self.__mediciones)} muestras"



