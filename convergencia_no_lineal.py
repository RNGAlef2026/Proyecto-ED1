
import numpy as np

from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Sistema no lineal de Lotka-Volterra
def sistema(t, u):
    x = u[0]
    y = u[1]

    dx = 0.8*x - 0.4*x*y
    dy = 0.2*x*y - 0.6*y

    return [dx, dy]


# Condiciones iniciales
t0 = 0
u0 = [2, 1]
t_final = 5

# Solucion numerica de referencia
h_ref = 0.0001
n_ref = round((t_final - t0) / h_ref)

referencia = rk4_sistemas(
    sistema, t0, u0, h_ref, n_ref
)

u_ref = referencia[-1][1]

print("Solucion numerica de referencia")
print(f"x(5) = {u_ref[0]:.10f}")
print(f"y(5) = {u_ref[1]:.10f}")


# Analisis de convergencia
pasos = [0.1, 0.05, 0.025, 0.0125]

errores_euler = []
errores_rk4 = []

print("\nAnalisis de convergencia")
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

    # Norma euclidiana del error estimado
    error_euler = np.linalg.norm(u_ref - u_euler)
    error_rk4 = np.linalg.norm(u_ref - u_rk4)

    errores_euler.append(error_euler)
    errores_rk4.append(error_rk4)

    print(
        f"{h:.4f}\t\t"
        f"{error_euler:.10f}\t"
        f"{error_rk4:.10f}"
    )


# Calculo de razones de convergencia
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
