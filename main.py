import math
import matplotlib.pyplot as plt

from euler import euler

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

# Datos de la grafica
tiempos = [t for t, y in resultados]
valores_euler = [y for t, y in resultados]
valores_exactos = [solucion_exacta(t) for t in tiempos]

# Crear la grafica
plt.plot(tiempos, valores_exactos, label="Solucion exacta")
plt.plot(tiempos, valores_euler, "o--", label="Metodo de Euler")

plt.title("Metodo de Euler vs Solucion exacta")
plt.xlabel("Tiempo (t)")
plt.ylabel("Solucion y(t)")
plt.legend()
plt.grid(True)

plt.show()