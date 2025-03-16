import pandas as pd
import numpy as np
import datetime
from faker import Faker

# Crear un generador de datos en español
fake = Faker("es_ES")

# Definir el número de hijos a generar
num_hijos = 30

# Generar ID_hijos (1 al 30)
id_hijos = np.arange(1, num_hijos + 1)

# Generar ID_empleado aleatoriamente (1 a 40), permitiendo que algunos se repitan hasta 5 veces
id_empleado = np.random.choice(np.arange(1, 41), size=num_hijos, replace=True)

# Generar nombres y apellidos ficticios
nombre_apellido = [fake.name() for _ in range(num_hijos)]

# Definir rango de fechas de nacimiento en formato datetime.date
fecha_inicio = datetime.date(1990, 1, 1)
fecha_fin = datetime.date(2025, 3, 16)

# Generar fechas de nacimiento aleatorias dentro del rango permitido
fecha_nacimiento = [fake.date_between(start_date=fecha_inicio, end_date=fecha_fin) for _ in range(num_hijos)]

# Crear el DataFrame
df_datos_hijos = pd.DataFrame({
    "ID_hijos": id_hijos,
    "ID_empleado": id_empleado,
    "Nombre_Apellido": nombre_apellido,
    "Fecha_nacimiento": fecha_nacimiento
})

# Guardar en CSV
df_datos_hijos.to_csv("Datos_Hijos.csv", index=False, encoding="utf-8")

# Mostrar las primeras filas para verificar
print(df_datos_hijos.head(10))
