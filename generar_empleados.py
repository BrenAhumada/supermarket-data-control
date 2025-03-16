import pandas as pd
import numpy as np
from faker import Faker

def main_function():
    # Crear un generador de datos ficticios en español
    fake = Faker("es_ES")

    # Definir el número de empleados
    num_empleados = 40

    # Generar ID de empleado (1 al 40)
    id_empleado = np.arange(1, num_empleados + 1)

    # Generar nombres y apellidos ficticios
    nombre_apellido = [fake.name() for _ in range(num_empleados)]

    # Generar DNI de 8 dígitos aleatorios
    dni = [fake.random_int(min=10000000, max=99999999) for _ in range(num_empleados)]

    # Generar domicilios ficticios
    domicilio = [fake.street_address() for _ in range(num_empleados)]

    # Lista de ciudades de Navarra
    ciudades_navarra = ["Pamplona", "Tudela", "Estella", "Alsasua", "Baztan", "Sangüesa", "Bera", "Elizondo"]
    ciudad = np.random.choice(ciudades_navarra, num_empleados)

    # País fijo: España
    pais = ["España"] * num_empleados

    # Generar ID_nacionalidad con mayor frecuencia en 1
    id_nacionalidad = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8], size=num_empleados, p=[0.5, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05])

    # Generar móvil (8 dígitos)
    movil = [fake.random_int(min=60000000, max=69999999) for _ in range(num_empleados)]

    # Generar correos electrónicos basados en nombres
    correo_electronico = [f"{nombre.lower().replace(' ', '_')}@ejemplo.com" for nombre in nombre_apellido]

    # Generar números de cuenta bancaria (21 dígitos) como texto para evitar formato científico en Excel/Power BI
    n_cuenta_bancaria = [f"'{''.join([str(fake.random_int(0, 9)) for _ in range(21)])}" for _ in range(num_empleados)]

    # Generar fechas de nacimiento entre 1965 y 2000
    fecha_nacimiento = [fake.date_between(start_date="-58y", end_date="-24y") for _ in range(num_empleados)]

    # Generar sexo aleatorio con mayor frecuencia en "Hombre" y "Mujer"
    sexo = np.random.choice(["Mujer", "Hombre", "No especifica"], size=num_empleados, p=[0.45, 0.45, 0.10])

    # ✅ Generar ID_puesto con más frecuencia en los valores entre 41 y 60
    id_puesto = np.random.choice(
        list(range(1, 41)) + list(range(41, 61)) * 3,  # Repetimos más veces 41-60
        size=num_empleados
    )

    # Crear el DataFrame
    df = pd.DataFrame({
        "ID_empleado": id_empleado,
        "Nombre_Apellido": nombre_apellido,
        "DNI": dni,
        "Domicilio": domicilio,
        "Ciudad": ciudad,
        "País": pais,
        "ID_nacionalidad": id_nacionalidad,
        "Móvil": movil,
        "Correo_electrónico": correo_electronico,
        "N_cuenta_bancaria": n_cuenta_bancaria,
        "Fecha_nacimiento": fecha_nacimiento,
        "Sexo": sexo,
        "ID_puesto": id_puesto  # Nueva columna con la distribución solicitada
    })

    # Guardar en CSV
    df.to_csv("Empleados.csv", index=False, encoding="utf-8")

    # Mostrar las primeras filas
    print(df.head())
    
if __name__ == '__main__':
    main_function()
