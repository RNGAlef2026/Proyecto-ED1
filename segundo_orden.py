import math
import matplotlib.pyplot as plt


from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Sistema equivalente a la ED de segundo orden
def sistema(t, u):
    u1 = u[0]
    u2 = u[1]

    du1 = u2
    du2 = -3*u2 - 2*u1

    return [du1, du2]

def solucion_exacta(t):
    return 2 * math.exp(-t) - math.exp(-2*t)

# Condiciones iniciales
t0 = 0
u0 = [1, 0]
h = 0.1
n = 5

# Resolver usando Euler
resultados = euler_sistemas(sistema, t0, u0, h, n)

print("Euler - Ecuacion de segundo orden")
print("-------------------------------------")
print("t\t y(t)\t\t y'(t)")

for t, u in resultados:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")

resultados_rk4 = rk4_sistemas(sistema, t0, u0, h, n)

print("\nRK4 - Ecuacion de segundo orden")
print("----------------------------------------")
print("t\t y(t)\t\t y'(t)")

for t, u in resultados_rk4:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")

print("\nComparacion con solucion analitica")
print("-" * 75)
print("t\t Euler\t\t RK4\t\t Exacta\t\t Error Euler\t Error RK4")

for i in range(len(resultados)):
    t = resultados[i][0]

    y_euler = resultados[i][1][0]
    y_rk4 = resultados_rk4[i][1][0]
    exacta = solucion_exacta(t)

    error_euler = abs(exacta - y_euler)
    error_rk4 = abs(exacta - y_rk4)

    print(
        f"{t:.2f}\t "
        f"{y_euler:.6f}\t "
        f"{y_rk4:.6f}\t "
        f"{exacta:.6f}\t "
        f"{error_euler:.6f}\t "
        f"{error_rk4:.6f}"
    )


# Datos para la grafica
tiempos = [t for t, u in resultados]

valores_euler = [u[0] for t, u in resultados]

valores_rk4 = [u[0] for t, u in resultados_rk4]

valores_exactos = [
    solucion_exacta(t) for t in tiempos
]

# Crear grafica comparativa
plt.plot(
    tiempos, valores_exactos,
    label="Solucion exacta",
    linewidth=2
)

plt.plot(
    tiempos, valores_euler,
    "o--",
    label="Metodo de Euler"
)

plt.plot(
    tiempos, valores_rk4,
    "s:",
    label="Metodo RK4"
)

plt.title("ED de segundo orden: Euler vs RK4")
plt.xlabel("Tiempo (t)")
plt.ylabel("Solucion y(t)")

plt.legend()
plt.grid(True)
plt.show()
