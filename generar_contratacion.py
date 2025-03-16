import pandas as pd
import numpy as np
import datetime
from faker import Faker

# Crear un generador de datos en español
fake = Faker("es_ES")

# Definir el número de empleados
num_empleados = 40

# Convertir las fechas a datetime.date
fecha_inicio = datetime.date(1980, 1, 1)
fecha_fin = datetime.date(2025, 3, 16)

# Generar ID de empleado (1 al 40)
id_empleado = np.arange(1, num_empleados + 1)

# Generar fechas de contratación correctamente
fecha_contratacion = [fake.date_between(start_date=fecha_inicio, end_date=fecha_fin) for _ in range(num_empleados)]

# Generar Tipo de contratación (ETT o Empresa) con probabilidades iguales
tipo_contratacion = np.random.choice(["ETT", "Empresa"], size=num_empleados)

# Generar Naturaleza del contrato con más frecuencia en "Transformación en indefinido"
naturaleza_contrato = np.random.choice(
    ["Transformación en indefinido", "Contrato de aprendizaje", "Discapacidad", "Duración indeterminada"],
    size=num_empleados,
    p=[0.5, 0.2, 0.15, 0.15]
)

# Generar Fecha de baja (solo si ID_empleado >= 30)
fecha_baja = [fake.date_between(start_date=datetime.date(1990, 1, 1), end_date=fecha_fin) if emp_id >= 30 else np.nan for emp_id in id_empleado]

# ✅ Corregido: Generar Motivo de baja SOLO si hay Fecha_baja
motivo_baja = [
    np.random.choice(["Jubilación", "Renuncia", "Despido", "Finalización del contrato"]) if not pd.isna(fecha_baja[i]) else np.nan
    for i in range(num_empleados)
]

# ✅ Corregido: Generar Fecha_fin_periodo_prueba SOLO si Motivo_baja = "Finalización del contrato"
fecha_fin_periodo_prueba = [
    (fecha_contratacion[i] + pd.DateOffset(months=6)) if motivo_baja[i] == "Finalización del contrato" else np.nan
    for i in range(num_empleados)
]

# Generar Horas de trabajo en función de la naturaleza del contrato
horas_trabajo = [
    4 if naturaleza_contrato[i] == "Contrato de aprendizaje" else
    6 if naturaleza_contrato[i] == "Discapacidad" else
    8
    for i in range(num_empleados)
]

# Crear el DataFrame
df_contratacion = pd.DataFrame({
    "ID_empleado": id_empleado,
    "Fecha_contratacion": fecha_contratacion,
    "Tipo_contratacion": tipo_contratacion,
    "Naturaleza_contrato": naturaleza_contrato,
    "Fecha_baja": fecha_baja,
    "Motivo_baja": motivo_baja,
    "Fecha_fin_periodo_prueba": fecha_fin_periodo_prueba,
    "Hs_trabajo": horas_trabajo
})

# Guardar en CSV
df_contratacion.to_csv("contratacion.csv", index=False, encoding="utf-8")

# Mostrar las primeras filas para verificar
print(df_contratacion.head(10))
