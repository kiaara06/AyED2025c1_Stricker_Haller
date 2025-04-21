def ordenamiento_Residual(lista):
    if not lista:
        return []

    # 1° determinar el numero maximo de digitos
    max_val = max(lista)
    num_digitos = len(str(max_val))

    # Ordenar por cada dígito, desde el menos significativo hasta el más significativo
    for posicion_del_digito in range(num_digitos):
        # Crear 10 buckets (uno para cada dígito del 0 al 9)
        buckets = [[] for _ in range(10)]

        # Distribuir los números en los buckets según el dígito actual
        for numero in lista:
            # Obtener el dígito en la posición actual
            digito = (numero // (10 ** posicion_del_digito)) % 10
            buckets[digito].append(numero)

        # Recolectar los números de los buckets en orden
        lista = []
        for bucket in buckets:
            lista.extend(bucket)

    return lista