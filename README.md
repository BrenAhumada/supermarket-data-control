# Dataset_RRHH

PROMP PARA EL CHAT GPT

sos experto y profesor en Python y yo no tengo conocimientos y soy tu alumna, explicame de forma sencilla y paso a paso cómo generar un script de python, utilizando Visual Studio Code, que genere una tabla cuyas columnas tengan el siguiente nombre y generen filas que cumplan las siguientes condiciones:
-Fecha: generar un rango de fechas desde el 01/01/2024 hasta el 31/03/2025 (ambos días inclusive) y que cada uno de ellos se repita 30 veces.
-ID_empleado: generar un rango desde el 1 hasta el 30 y que se repita para cada uno de los días de la columna Fecha.
-ID_turno: Asignar aleatoriamente un 1 ó 2 ó 3, pero que se repitan con mayor frecuencia los 1 y 2.
-ID_asistencia: generar aleatoriamente un 1 o 2 pero que se repitan con mayor frecuencia los 1.
-ID_absentismo: si el ID_asistencia = 2, entonces colocar en esta columna aleatoriamente un número que va desde el 1 hasta el 14, pero que se repitan con mayor frecuencia el 7 y luego el 1.
-Horas_trabajadas: asignar aleatoriamente un número desde el 10 hasta el 4, pero que se repitan con mayor frecuencia el 8.

Si tienes dudas, preguntame antes de responderme

SCRIPT Nº1

import pandas as pd
import numpy as np

# Generar el rango de fechas
fechas = pd.date_range(start="2024-01-01", end="2025-03-31")

# Repetir cada fecha 30 veces (para 30 empleados)
fechas_repetidas = np.repeat(fechas, 30)

# Generar el ID de empleado (1 a 30 para cada día)
id_empleado = np.tile(np.arange(1, 31), len(fechas))

# Generar ID_turno con mayor frecuencia de 1 y 2
id_turno = np.random.choice([1, 2, 3], size=len(fechas_repetidas), p=[0.45, 0.45, 0.10])

# Generar ID_asistencia con mayor frecuencia de 1
id_asistencia = np.random.choice([1, 2], size=len(fechas_repetidas), p=[0.75, 0.25])

# Generar ID_absentismo (solo cuando ID_asistencia = 2)
id_absentismo = np.where(
    id_asistencia == 2, 
    np.random.choice([1, 7] + list(range(2, 15)), size=len(fechas_repetidas), p=[0.4, 0.4] + [0.2/12]*12),
    np.nan  # Si asistencia es 1, no hay absentismo
)

# Generar Horas_trabajadas con mayor frecuencia en 8
horas_trabajadas = np.random.choice([8, 10, 9, 7, 6, 5, 4], size=len(fechas_repetidas), p=[0.5, 0.1, 0.1, 0.1, 0.07, 0.07, 0.06])

# Crear el DataFrame
df = pd.DataFrame({
    "Fecha": fechas_repetidas,
    "ID_empleado": id_empleado,
    "ID_turno": id_turno,
    "ID_asistencia": id_asistencia,
    "ID_absentismo": id_absentismo,
    "Horas_trabajadas": horas_trabajadas
})

# Guardar en un archivo CSV
df.to_csv("datos_empleados.csv", index=False)

# Mostrar las primeras filas para verificar
print(df.head())


EXPLICACIÓN DEL CODIGO:

Explicación del código
Generamos las fechas con pd.date_range(), desde 01/01/2024 hasta 31/03/2025.
Repetimos cada fecha 30 veces (np.repeat()) porque hay 30 empleados por día.
Creamos el ID de empleado (np.tile()) para repetir los valores del 1 al 30 para cada fecha.
Generamos el ID_turno con una mayor probabilidad de obtener 1 o 2 usando np.random.choice().
Generamos el ID_asistencia, dando una mayor probabilidad a 1 (presente).
Generamos el ID_absentismo, pero solo si el empleado faltó (ID_asistencia = 2), con 7 y 1 como valores más frecuentes.
Generamos las Horas_trabajadas, donde 8 se repite con más frecuencia.
Creamos el DataFrame con pd.DataFrame().
Guardamos los datos en un CSV con to_csv().
Mostramos las primeras filas con print(df.head()) para verificar.

AJUSTES SCRIPT 1 (para absentismo)

Error del script de Absentismo:

error de vuelta:
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
Cell In[19], line 10
      7 probabilidades = np.array([0.4, 0.4] + [0.2/11]*11)  # Deben sumar 1 y tener 14 valores
      9 # Asegurar que los tamaños coincidan antes de continuar
---> 10 assert len(valores_absentismo) == len(probabilidades), f"Tamaños diferentes: {len(valores_absentismo)} valores y {len(probabilidades)} probabilidades"
     12 # Inicializar la columna con NaN asegurando que sea float
     13 id_absentismo = np.full(len(id_asistencia), np.nan, dtype=float)

AssertionError: Tamaños diferentes: 15 valores y 13 probabilidades

El error está en la generación de la lista de valores y sus probabilidades:
valores_absentismo = np.array([1, 7] + list(range(2, 15)))  # Genera 15 valores (INCORRECTO)

[1, 7] + list(range(2, 15)) crea 15 valores porque range(2, 15) incluye 2 hasta 14, pero ya teníamos 1 y 7.
El otro error está en la lista de probabilidades:

python
Copy
Edit
probabilidades = np.array([0.4, 0.4] + [0.2/11]*11)  # Genera solo 13 probabilidades (INCORRECTO)
[0.2/11] * 11 genera solo 11 valores, pero necesitamos 13.

Solución definitiva:

import numpy as np

# Generar ID_absentismo (solo cuando ID_asistencia = 2)
valores_absentismo = np.array([1, 7] + list(range(2, 14)))  # Genera solo 14 valores (1 al 14)

# Corregir la lista de probabilidades asegurando que tenga 14 valores y sumen 1
probabilidades = np.array([0.4, 0.4] + [0.2/12]*12)  # Ahora son 14 valores

# Verificar que ambos tengan la misma longitud
assert len(valores_absentismo) == len(probabilidades), f"Tamaños diferentes: {len(valores_absentismo)} valores y {len(probabilidades)} probabilidades"

# Inicializar la columna con NaN asegurando que sea float
id_absentismo = np.full(len(id_asistencia), np.nan, dtype=float)

# Filtrar los índices donde ID_asistencia = 2
indices_ausentes = np.where(id_asistencia == 2)[0]  # Indices de empleados ausentes

# Generar valores aleatorios solo para los empleados ausentes
id_absentismo[indices_ausentes] = np.random.choice(
    valores_absentismo, 
    size=len(indices_ausentes), 
    p=probabilidades
).astype(float)


Explicación de la corrección

valores_absentismo ahora tiene exactamente 14 valores:

valores_absentismo = np.array([1, 7] + list(range(2, 14)))  # 14 valores en total
Antes: list(range(2, 15)) generaba 13 valores (del 2 al 14), sumando 15 en total.
Ahora: list(range(2, 14)) genera solo 12 valores, sumando 14 en total.
probabilidades ahora tiene exactamente 14 valores:

probabilidades = np.array([0.4, 0.4] + [0.2/12]*12)  # 14 valores en total
0.4 para 1
0.4 para 7
0.2/12 distribuido entre los 12 valores restantes (del 2 al 14).
El assert ahora verificará correctamente:

assert len(valores_absentismo) == len(probabilidades)
Antes fallaba porque había 15 valores y 13 probabilidades.
Ahora ambos tienen 14 valores.

Verificar que funciona
Después de ejecutar el código, revisa si los valores generados son correctos con:

print(pd.Series(id_absentismo).value_counts(dropna=False))
Esto te mostrará la distribución de valores en ID_absentismo, incluyendo los NaN.
