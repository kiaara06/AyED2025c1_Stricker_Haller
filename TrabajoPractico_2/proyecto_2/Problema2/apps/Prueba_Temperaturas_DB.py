from modules.Temperaturas_DB import Temperaturas_DB

if __name__=="__main__":
    T = Temperaturas_DB()
    T.guardar_temperatura(22.5,"16/06/2025")
    T.guardar_temperatura(55.5,"29/05/2025")
    T.guardar_temperatura(17.5,"13/07/2025")
    T.guardar_temperatura(20.5,"15/10/2025")

    print(T.devolver_temperatura("15/10/2025"))

    print(T.max_temp_rango("29/05/2025","16/06/2025"))

    print(T.min_temp_rango("29/05/2025","16/06/2025"))

    print(T.temp_extremos_rango("29/05/2025","16/06/2025"))

    print(T.cantidad_muestras())

    print(T.devolver_temperaturas("29/05/2025","15/10/2025"))

    print(T.borrar_temperatura("13/07/2025"))

    print(T.devolver_temperaturas("29/05/2025","15/10/2025"))
