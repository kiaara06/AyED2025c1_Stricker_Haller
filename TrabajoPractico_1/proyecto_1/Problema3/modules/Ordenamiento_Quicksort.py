def ordenamiento_Quicksort(lista):
    if len(lista) <= 1: 
        return lista
    else:
        pivote = lista[0] 
        menores = [x for x in lista[1:] if x < pivote] 
        mayores = [x for x in lista[1:] if x >= pivote] 
        return ordenamiento_Quicksort(menores) + [pivote] + ordenamiento_Quicksort(mayores)