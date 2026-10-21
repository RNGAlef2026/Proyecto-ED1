
def euler(f, t0, y0, h, n):
    """
    Resuelve una EDO de primer orden mediante el metodo de Euler.

    Parametros:
        f: funcion que representa la derivada y' = f(t, y).
        t0: valor inicial de la variable independiente.
        y0: condicion inicial de la ecuacion diferencial.
        h: tamano del paso de integracion.
        n: numero de iteraciones.

    Retorna:
        Lista de tuplas (t, y) con las aproximaciones
        numericas, incluyendo la condicion inicial.

    Limitaciones:
        Es un metodo explicito de primer orden.
        Su precision y estabilidad dependen del paso h.
    """

    if h <= 0:
        raise ValueError("El tamano del paso debe ser positivo.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")

    t = t0
    y = y0

    resultados = [(t, y)]

    for i in range(n):
        y_nuevo = y + h * f(t, y)
        t_nuevo = t + h

        t = t_nuevo
        y = y_nuevo

        resultados.append((t, y))

    return resultados
