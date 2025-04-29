def flatten(lista):
    """
    Función recursiva que aplana una lista anidada.
    """
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(flatten(elemento))
        else:
            resultado.append(elemento)
    return resultado
