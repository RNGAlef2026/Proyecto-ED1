def runge_kutta4(f, t0, y0, h, n):
    """
    Resuelve una EDO de primer orden usando RK4.

    Parametros:
        f: funcion de la ecuacion diferencial
        t0: valor inicial de t
        y0: condicion inicial
        h: tamano del paso
        n: numero de iteraciones

    Retorna:
        Lista de pares (t, y) calculados.
    """

    t = t0
    y = y0

    resultados = [(t, y)]

    for i in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h, y + h*k3)

        y_nuevo = y + (h/6*(k1 + 2*k2 + 2*k3 + k4))
        t_nuevo = t + h

        t = t_nuevo
        y = y_nuevo

        resultados.append((t, y))

    return resultados



