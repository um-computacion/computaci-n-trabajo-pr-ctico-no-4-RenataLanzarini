def factorial_recursivo(n: int) -> int:
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial del número.

    Raises:
        ValueError: Si el número es negativo.
    """
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


def factorial_no_recursivo(n: int) -> int:
    """
    Calcula el factorial de un número de forma iterativa.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial del número.

    Raises:
        ValueError: Si el número es negativo.
    """
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    
    total = 1
    for i in range(2, n + 1):
        total *= i
    return total
    
