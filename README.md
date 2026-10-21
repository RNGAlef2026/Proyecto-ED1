# Proyecto Final - Ecuaciones Diferenciales 1

## Descripción

Este proyecto implementa y compara dos métodos numéricos iterativos para resolver ecuaciones diferenciales ordinarias (EDO) utilizando Python:

- Método de Euler.
- Método de Runge-Kutta de cuarto orden (RK4).

El objetivo es analizar la precisión, los errores numéricos y la convergencia de ambos métodos mediante cuatro problemas matemáticos.

## Tecnologías utilizadas

- Python 3
- NumPy
- Matplotlib
- Git y GitHub

## Problemas implementados

### 1. Ecuación diferencial de primer orden

Ecuación:

`y' = t + y`

Condición inicial: `y(0) = 1`

Solución analítica:

`y(t) = 2e^t - t - 1`

Archivo: `main.py`

### 2. Ecuación diferencial de segundo orden

Ecuación:

`y'' + 3y' + 2y = 0`

Condiciones iniciales:

`y(0) = 1`, `y'(0) = 0`

Solución analítica:

`y(t) = 2e^(-t) - e^(-2t)`

Archivo: `segundo_orden.py`

### 3. Sistema lineal 2x2

Sistema:

`x' = 3x + 2y`

`y' = 2x + 3y`

Condiciones iniciales:

`x(0) = 1`, `y(0) = 0`

Archivos: `sistema_lineal.py` y `convergencia_lineal.py`

### 4. Sistema no lineal 2x2

Modelo de Lotka-Volterra:

`x' = 0.8x - 0.4xy`

`y' = 0.2xy - 0.6y`

Condiciones iniciales:

`x(0) = 2`, `y(0) = 1`

Se analiza la convergencia mediante una solución numérica de referencia obtenida con RK4.

Archivos: `sistema_no_lineal.py` y `convergencia_no_lineal.py`

## Instalación

Clonar el repositorio desde GitHub:

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar a la carpeta del proyecto:

```bash
cd Proyecto_ED1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Para ejecutar los cuatro problemas:

```bash
python main.py
python segundo_orden.py
python sistema_lineal.py
python sistema_no_lineal.py
```

Para ejecutar los análisis de convergencia:

```bash
python convergencia.py
python convergencia_segundo_orden.py
python convergencia_lineal.py
python convergencia_no_lineal.py
```

Para validar la solución numérica de referencia:

```bash
python validacion_referencia.py
```

## Análisis numérico

Los programas permiten:

- Comparar aproximaciones numéricas con soluciones analíticas cuando están disponibles.
- Calcular errores absolutos.
- Analizar la convergencia al reducir el tamaño de paso.
- Generar gráficas comparativas.
- Estudiar el comportamiento de un sistema no lineal sin solución explícita general sencilla.

Los resultados obtenidos son consistentes con los órdenes de convergencia global esperados: orden 1 para Euler y orden 4 para RK4.

## Integrantes

- Integrante 1
- Integrante 2
- Integrante 3

## Curso

Ecuaciones Diferenciales 1 — Segundo ciclo 2026.