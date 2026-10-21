def euler (f, t0, y0, h, n):
    """
    Resuelve una EDO de primer orden usando Euler.

    Parametros:
        f: funcion de la ecuacion diferencial
        t0: valor inicial de t
        y0: condicion inicial
        h: tamano del paso
        n: numero de iteraciones

    Retorna:
        Lista de pares (t, y) calculados
    """

    t = t0
    y= y0

    resultados = [(t, y)]

    for i in range(n):
        y_nuevo = y + h * f(t, y)
        t_nuevo = t + h

        t = t_nuevo
        y = y_nuevo

        resultados.append((t, y))

    return resultados