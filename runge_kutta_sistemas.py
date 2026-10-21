
import numpy as np


def rk4_sistemas(f, t0, u0, h, n):
    """
    Resuelve sistemas de EDOs mediante Runge-Kutta
    de cuarto orden (RK4).

    Parametros:
        f: funcion que representa el sistema u' = f(t, u).
        t0: valor inicial de la variable independiente.
        u0: vector de condiciones iniciales.
        h: tamano del paso de integracion.
        n: numero de iteraciones.

    Retorna:
        Lista de tuplas (t, u) con las aproximaciones
        numericas, incluyendo las condiciones iniciales.

    Limitaciones:
        Es un metodo explicito de cuarto orden.
        Su precision y estabilidad dependen del paso h.
        Requiere cuatro evaluaciones de f por paso.
        El sistema debe estar expresado en primer orden.
    """

    if h <= 0:
        raise ValueError("El tamano del paso debe ser positivo.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")

    t = t0
    u = np.array(u0, dtype=float)

    if u.ndim != 1 or u.size == 0:
        raise ValueError("u0 debe ser un vector no vacio.")

    resultados = [(t, u.copy())]

    def evaluar(t_actual, u_actual):
        derivadas = np.asarray(
            f(t_actual, u_actual), dtype=float
        )

        if derivadas.shape != u.shape:
            raise ValueError(
                "La funcion debe devolver un vector "
                "del mismo tamano que u0."
            )

        return derivadas

    for i in range(n):
        k1 = evaluar(t, u)

        k2 = evaluar(
            t + h/2, u + h*k1/2
        )

        k3 = evaluar(
            t + h/2, u + h*k2/2
        )

        k4 = evaluar(
            t + h, u + h*k3
        )

        u_nuevo = u + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t_nuevo = t + h

        t = t_nuevo
        u = u_nuevo

        resultados.append((t, u.copy()))

    return resultados