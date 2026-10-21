
import math
import matplotlib.pyplot as plt

from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Sistema de ecuaciones diferenciales
def sistema(t, u):
    x = u[0]
    y = u[1]

    dx = 3*x + 2*y
    dy = 2*x + 3*y

    return [dx, dy]


# Soluciones analiticas
def solucion_exacta_x(t):
    return (math.exp(5*t) + math.exp(t)) / 2


def solucion_exacta_y(t):
    return (math.exp(5*t) - math.exp(t)) / 2


# Condiciones iniciales
t0 = 0
u0 = [1, 0]
h = 0.1
n = 5


# Resolver con ambos metodos
resultados_euler = euler_sistemas(sistema, t0, u0, h, n)

resultados_rk4 = rk4_sistemas(sistema, t0, u0, h, n)


# Mostrar resultados de Euler
print("Euler - Sistema lineal 2x2")
print("-" * 45)
print("t\t x(t)\t\t y(t)")

for t, u in resultados_euler:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")


# Mostrar resultados de RK4
print("\nRK4 - Sistema lineal 2x2")
print("-" * 45)
print("t\t x(t)\t\t y(t)")

for t, u in resultados_rk4:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")



# Comparacion con soluciones analiticas
print("\nComparacion de resultados")
print("-" * 80)

for i in range(len(resultados_euler)):
    t = resultados_euler[i][0]

    x_euler = resultados_euler[i][1][0]
    y_euler = resultados_euler[i][1][1]

    x_rk4 = resultados_rk4[i][1][0]
    y_rk4 = resultados_rk4[i][1][1]

    x_exacta = solucion_exacta_x(t)
    y_exacta = solucion_exacta_y(t)

    error_x_euler = abs(x_exacta - x_euler)
    error_y_euler = abs(y_exacta - y_euler)

    error_x_rk4 = abs(x_exacta - x_rk4)
    error_y_rk4 = abs(y_exacta - y_rk4)

    print(f"\nt = {t:.2f}")

    print(
        f"x: Exacta={x_exacta:.6f} | "
        f"Euler={x_euler:.6f} | "
        f"RK4={x_rk4:.6f}"
    )

    print(
        f"   Error Euler={error_x_euler:.6f} | "
        f"Error RK4={error_x_rk4:.6f}"
    )

    print(
        f"y: Exacta={y_exacta:.6f} | "
        f"Euler={y_euler:.6f} | "
        f"RK4={y_rk4:.6f}"
    )

    print(
        f"   Error Euler={error_y_euler:.6f} | "
        f"Error RK4={error_y_rk4:.6f}"
    )


# Preparar datos
tiempos = [t for t, u in resultados_euler]

x_euler = [u[0] for t, u in resultados_euler]
y_euler = [u[1] for t, u in resultados_euler]

x_rk4 = [u[0] for t, u in resultados_rk4]
y_rk4 = [u[1] for t, u in resultados_rk4]

x_exacta = [solucion_exacta_x(t) for t in tiempos]
y_exacta = [solucion_exacta_y(t) for t in tiempos]


# Grafica de x(t)
plt.figure()

plt.plot(tiempos, x_exacta, label="Solucion exacta")
plt.plot(tiempos, x_euler, "o--", label="Euler")
plt.plot(tiempos, x_rk4, "s:", label="RK4")

plt.title("Sistema lineal 2x2 - Variable x(t)")
plt.xlabel("Tiempo (t)")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)


# Grafica de y(t)
plt.figure()

plt.plot(tiempos, y_exacta, label="Solucion exacta")
plt.plot(tiempos, y_euler, "o--", label="Euler")
plt.plot(tiempos, y_rk4, "s:", label="RK4")

plt.title("Sistema lineal 2x2 - Variable y(t)")
plt.xlabel("Tiempo (t)")
plt.ylabel("y(t)")
plt.legend()
plt.grid(True)

plt.show()
