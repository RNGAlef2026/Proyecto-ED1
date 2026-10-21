
import math

from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Sistema equivalente a la ED de segundo orden
def sistema(t, u):
    u1 = u[0]
    u2 = u[1]

    du1 = u2
    du2 = -3*u2 - 2*u1

    return [du1, du2]


# Solucion analitica
def solucion_exacta(t):
    return 2 * math.exp(-t) - math.exp(-2*t)


# Condiciones iniciales
t0 = 0
u0 = [1, 0]
t_final = 0.5

# Tamanos de paso
pasos = [0.1, 0.05, 0.025, 0.0125]

# Listas para guardar errores
errores_euler = []
errores_rk4 = []

print("Convergencia - ED de segundo orden")
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

    # Primera componente: y(t)
    y_euler = resultados_euler[-1][1][0]
    y_rk4 = resultados_rk4[-1][1][0]

    exacta = solucion_exacta(t_final)

    # Calcular errores absolutos
    error_euler = abs(exacta - y_euler)
    error_rk4 = abs(exacta - y_rk4)

    errores_euler.append(error_euler)
    errores_rk4.append(error_rk4)

    print(
        f"{h:.4f}\t\t"
        f"{error_euler:.10f}\t"
        f"{error_rk4:.10f}"
    )


# Calcular razones de convergencia
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
