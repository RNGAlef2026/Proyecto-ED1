import matplotlib.pyplot as plt

from euler_sistemas import euler_sistemas
from runge_kutta_sistemas import rk4_sistemas


# Modelo depredador-presa de Lotka-Volterra
def sistema(t, u):
    x = u[0]
    y = u[1]

    dx = 0.8*x - 0.4*x*y
    dy = 0.2*x*y - 0.6*y

    return [dx, dy]


# Condiciones iniciales
t0 = 0
u0 = [2, 1]

# Parametros numericos
h = 0.1
n = 50


# Resolver con Euler
resultados_euler = euler_sistemas(
    sistema, t0, u0, h, n
)

# Resolver con Runge-Kutta 4
resultados_rk4 = rk4_sistemas(
    sistema, t0, u0, h, n
)


# Mostrar resultados de Euler
print("Euler - Sistema no lineal 2x2")
print("-" * 45)
print("t\t x(t)\t\t y(t)")

for t, u in resultados_euler:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")


# Mostrar resultados de RK4
print("\nRK4 - Sistema no lineal 2x2")
print("-" * 45)
print("t\t x(t)\t\t y(t)")

for t, u in resultados_rk4:
    print(f"{t:.2f}\t {u[0]:.6f}\t {u[1]:.6f}")


# Preparar los datos
tiempos = [t for t, u in resultados_euler]

x_euler = [u[0] for t, u in resultados_euler]
y_euler = [u[1] for t, u in resultados_euler]

x_rk4 = [u[0] for t, u in resultados_rk4]
y_rk4 = [u[1] for t, u in resultados_rk4]


# Grafica de las presas
plt.figure()

plt.plot(tiempos, x_euler, "o--",
         label="Euler", markersize=3)

plt.plot(tiempos, x_rk4,
         label="RK4", linewidth=2)

plt.title("Sistema no lineal - Poblacion de presas")
plt.xlabel("Tiempo (t)")
plt.ylabel("Poblacion x(t)")
plt.legend()
plt.grid(True)

plt.savefig(
    "no_lineal_presas.png",
    dpi=300,
    bbox_inches="tight"
)

# Grafica de los depredadores
plt.figure()

plt.plot(tiempos, y_euler, "o--",
         label="Euler", markersize=3)

plt.plot(tiempos, y_rk4,
         label="RK4", linewidth=2)

plt.title("Sistema no lineal - Poblacion de depredadores")
plt.xlabel("Tiempo (t)")
plt.ylabel("Poblacion y(t)")
plt.legend()
plt.grid(True)

plt.savefig(
    "no_lineal_depredadores.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
