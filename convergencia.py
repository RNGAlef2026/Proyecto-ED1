
from euler import euler
from runge_kutta import runge_kutta4
import math


# Ecuacion diferencial
def f(t, y):
    return t + y


# Solucion analitica
def solucion_exacta(t):
    return 2 * math.exp(t) - t - 1


# Condiciones iniciales
t0 = 0
y0 = 1
t_final = 0.5

# Diferentes tamanos de paso
pasos = [0.1, 0.05, 0.025, 0.0125]

# Listas para almacenar los errores
errores_euler = []
errores_rk4 = []

print("Analisis de convergencia")
print("-" * 55)
print("h\t\tError Euler\tError RK4")

# Calculo de errores
for h in pasos:
    n = round((t_final - t0) / h)

    resultados_euler = euler(f, t0, y0, h, n)
    resultados_rk4 = runge_kutta4(f, t0, y0, h, n)

    y_euler = resultados_euler[-1][1]
    y_rk4 = resultados_rk4[-1][1]

    exacta = solucion_exacta(t_final)

    error_euler = abs(exacta - y_euler)
    error_rk4 = abs(exacta - y_rk4)

    # Guardar errores
    errores_euler.append(error_euler)
    errores_rk4.append(error_rk4)

    print(f"{h:.4f}\t\t{error_euler:.8f}\t{error_rk4:.10f}")


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
