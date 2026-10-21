import math
import matplotlib.pyplot as plt

from euler import euler
from runge_kutta import runge_kutta4

def solucion_exacta(t):
    return 2 * math.exp(t) - t - 1

def f(t, y):
    return t + y

t0 = 0
y0 = 1
h = 0.1
n = 5

resultados = euler(f, t0, y0, h, n)

print("Metodo de Euler")
print("----------------------")
print("t\t Euler\t\t Exacta\t\t Error")

for t, y in resultados:
    exacta = solucion_exacta(t)
    error = abs(exacta - y)

    print(f"{t:.2f}\t {y:.6f}\t {exacta:.6f}\t {error:.6f}")

# Prueba del metodo Runge-kutta 4
resultados_rk4 = runge_kutta4(f, t0, y0, h, n)

print("\nMetodo de Runge-Kutta 4")
print("--------------------------------")
print("t\t RK4\t\t Exacta\t\t Error")

for t, y in resultados_rk4:
    exacta = solucion_exacta(t)
    error = abs(exacta - y)

    print(f"{t:.2f}\t {y:.6f}\t {exacta:.6f}\t {error:.6f}")


# Datos para las graficas
tiempos = [t for t, y in resultados]

valores_euler = [y for t, y in resultados]

valores_rk4 = [y for t, y in resultados_rk4]

valores_exactos = [
    solucion_exacta(t) for t in tiempos
]

# Grafica comparativa
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

plt.title("Comparacion de metodos numericos")
plt.xlabel("Tiempo (t)")
plt.ylabel("Solucion y(t)")

plt.legend()
plt.grid(True)
plt.show()
