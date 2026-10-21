
import numpy as np

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

# Tamanos de paso para la validacion
h1 = 0.0001
h2 = 0.00005

n1 = round((t_final - t0) / h1)
n2 = round((t_final - t0) / h2)


# Primera aproximacion con RK4
resultados_1 = rk4_sistemas(
    sistema, t0, u0, h1, n1
)

# Segunda aproximacion con RK4
resultados_2 = rk4_sistemas(
    sistema, t0, u0, h2, n2
)


# Valores finales
u1 = resultados_1[-1][1]
u2 = resultados_2[-1][1]


# Diferencias entre aproximaciones
diferencia_x = abs(u1[0] - u2[0])
diferencia_y = abs(u1[1] - u2[1])

diferencia_total = np.linalg.norm(u1 - u2)


# Mostrar resultados
print("Validacion de referencia numerica")
print("-" * 55)

print(f"RK4 con h = {h1}")
print(f"x(5) = {u1[0]:.12f}")
print(f"y(5) = {u1[1]:.12f}")

print(f"\nRK4 con h = {h2}")
print(f"x(5) = {u2[0]:.12f}")
print(f"y(5) = {u2[1]:.12f}")

print("\nDiferencias entre aproximaciones")
print(f"Diferencia en x = {diferencia_x:.12e}")
print(f"Diferencia en y = {diferencia_y:.12e}")
print(f"Norma euclidiana = {diferencia_total:.12e}")
