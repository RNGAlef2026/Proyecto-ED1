
import math
import numpy as np

from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Sistema lineal 2x2
def sistema(t, u):
    x = u[0]
    y = u[1]

    dx = 3*x + 2*y
    dy = 2*x + 3*y

    return [dx, dy]


# Solucion analitica
def solucion_exacta(t):
    x = (math.exp(5*t) + math.exp(t)) / 2
    y = (math.exp(5*t) - math.exp(t)) / 2

    return np.array([x, y])


# Condiciones iniciales
t0 = 0
u0 = [1, 0]
t_final = 0.5

# Tamanos de paso
pasos = [0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125]

# Listas para almacenar errores
errores_euler = []
errores_rk4 = []

# Solucion exacta en el tiempo final
u_exacta = solucion_exacta(t_final)

print("Convergencia - Sistema lineal 2x2")
print("-" * 55)
print("h\t\tError Euler\tError RK4")

for h in pasos:
    n = round((t_final - t0) / h)

    resultados_euler = euler_sistemas(
        sistema, t0, u0, h, n
    )

    resultados_rk4 = rk4_sistemas(
        sistema, t0, u0, h, n
    )

    u_euler = resultados_euler[-1][1]
    u_rk4 = resultados_rk4[-1][1]

    # Norma euclidiana del error
    error_euler = np.linalg.norm(u_exacta - u_euler)
    error_rk4 = np.linalg.norm(u_exacta - u_rk4)

    errores_euler.append(error_euler)
    errores_rk4.append(error_rk4)

    print(
        f"{h:.4f}\t\t"
        f"{error_euler:.10f}\t"
        f"{error_rk4:.10f}"
    )


# Razones de convergencia
print("\nRazones de convergencia")
print("-" * 45)
print("h anterior\tEuler\t\tRK4")

for i in range(len(pasos) - 1):
    razon_euler = errores_euler[i] / errores_euler[i + 1]
    razon_rk4 = errores_rk4[i] / errores_rk4[i + 1]

    print(
        f"{pasos[i]:.4f}\t\t"
        f"{razon_euler:.4f}\t\t"
        f"{razon_rk4:.4f}"
    )
