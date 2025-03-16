import pandas as pd
import numpy as np

def main_function():
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


if __name__ == '__main__':
    main_function()

