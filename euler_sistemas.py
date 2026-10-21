import numpy as np

def euler_sistemas(f, t0, u0, h, n):
    """
    Resuelve sistemas de EDOs usando Euler.

    Parametros:
        f: funcion que representa el sistema
        t0: valor inicial de t
        u0: vector de condiciones iniciales
        h: tamano del paso
        n: numero de iteraciones

    Retorna:
        Lista de pares (t, u) calculados
    """

    t = t0
    u = np.array(u0, dtype=float)

    resultados = [(t, u.copy())]

    for i in range(n):
        u_nuevo = u +h * np.array(f(t, u))

        t_nuevo = t + h

        t = t_nuevo
        u = u_nuevo

        resultados.append((t, u.copy()))

    return resultados