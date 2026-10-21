
def runge_kutta4(f, t0, y0, h, n):
    """
    Resuelve una EDO de primer orden mediante
    Runge-Kutta de cuarto orden (RK4).

    Parametros:
        f: funcion que representa y' = f(t, y).
        t0: valor inicial de la variable independiente.
        y0: condicion inicial de la ecuacion diferencial.
        h: tamano del paso de integracion.
        n: numero de iteraciones.

    Retorna:
        Lista de tuplas (t, y) con las aproximaciones
        numericas, incluyendo la condicion inicial.

    Limitaciones:
        Es un metodo explicito de cuarto orden.
        Su precision y estabilidad dependen del paso h.
        Requiere cuatro evaluaciones de f por paso.
    """

    if h <= 0:
        raise ValueError("El tamano del paso debe ser positivo.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo.")

    t = t0
    y = y0

    resultados = [(t, y)]

    for i in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h*k1/2)
        k3 = f(t + h/2, y + h*k2/2)
        k4 = f(t + h, y + h*k3)

        y_nuevo = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t_nuevo = t + h

        t = t_nuevo
        y = y_nuevo

        resultados.append((t, y))

    return resultados