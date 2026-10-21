
import numpy as np


def rk4_sistemas(f, t0, u0, h, n):
    """
    Resuelve sistemas de EDOs usando RK4.

    Parametros:
        f: funcion que representa el sistema
        t0: valor inicial de t
        u0: vector de condiciones iniciales
        h: tamano del paso
        n: numero de iteraciones

    Retorna:
        Lista de pares (t, u) calculados.
    """

    t = t0
    u = np.array(u0, dtype=float)

    resultados = [(t, u.copy())]

    for i in range(n):
        k1 = np.array(f(t, u))

        k2 = np.array(
            f(t + h/2, u + h*k1/2)
        )

        k3 = np.array(
            f(t + h/2, u + h*k2/2)
        )

        k4 = np.array(
            f(t + h, u + h*k3)
        )

        u_nuevo = u + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t_nuevo = t + h

        t = t_nuevo
        u = u_nuevo

        resultados.append((t, u.copy()))

    return resultados
