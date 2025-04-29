def fibonacci_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser un número no negativo")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_no_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser un número no negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
