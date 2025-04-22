import random

#Ordenamiento Burbuja
def ordenamiento_Burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Ordenamiento Qicksort
def ordenamiento_Quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
        return ordenamiento_Quicksort(menores) + [pivote] + ordenamiento_Quicksort(mayores)

#Ordenamiento Burbuja
def ordenamiento_Residual(lista):
    if not lista:
        return []

    max_val = max(lista)
    num_digitos = len(str(max_val))

    for posicion_del_digito in range(num_digitos):
        buckets = [[] for _ in range(10)]
        for numero in lista:
            digito = (numero // (10 ** posicion_del_digito)) % 10
            buckets[digito].append(numero)

        lista = []
        for bucket in buckets:
            lista.extend(bucket)

    return lista


#GENERAMOS UNA LISTA ALEATORIA DE 500 NÚMEROS DE 5 DÍGITOS:
lista_original = [random.randint(10000, 99999) for _ in range(500)]

#Para verificar el correcto funcionamiento de los algoritmos implementados, 
# se compararon sus resultados con los obtenidos mediante la función sorted() de Python.

# Burbuja
lista_burbuja = ordenamiento_Burbuja(lista_original.copy())
print("¿Burbuja ordena bien?", lista_burbuja == sorted(lista_original))

# Quicksort
lista_quicksort = ordenamiento_Quicksort(lista_original.copy())
print("¿Quicksort ordena bien?", lista_quicksort == sorted(lista_original))

# Radix (residual)
lista_residual = ordenamiento_Residual(lista_original.copy())
print("¿Residual ordena bien?", lista_residual == sorted(lista_original))
