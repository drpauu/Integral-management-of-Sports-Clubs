import psycopg2
from faker import Faker
import random
from datetime import datetime

# Crear una instancia de Faker
fake = Faker()

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="est_e7594959",
    user="est_e7594959",
    password="dB.e7594959",
    host="localhost"
)
cur = conn.cursor()

# Generar datos ficticios
num_soci_range = range(10000, 100000)  # 10000 a 99999, incluyendo ambos

# Insertar membres
membres = []
for num_soci in num_soci_range:
    nom = fake.name()
    data_naixement = fake.date_of_birth(minimum_age=18, maximum_age=60)
    sexe = random.choice(['M', 'F'])
    email = fake.unique.email()

    try:
        cur.execute("""
            INSERT INTO practica.membre (num_soci, nom, data_naixement, sexe, email)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (num_soci) DO NOTHING
        """, (num_soci, nom, data_naixement, sexe, email))
        membres.append(num_soci)
    except psycopg2.errors.UniqueViolation:
        conn.rollback()

# Confirmar la inserción de los miembros antes de continuar
conn.commit()

# Verificar que todos los números de socio se hayan insertado correctamente
cur.execute("SELECT num_soci FROM practica.membre")
membres = [row[0] for row in cur.fetchall()]

# Insertar cuotas anuales
for membre in membres:
    for _ in range(random.randint(1, 3)):  # Cada miembro puede tener entre 1 y 3 cuotas anuales
        data_pagament = fake.date_between(start_date='-3y', end_date='today')
        importe = round(random.uniform(50, 150), 2)  # Importe entre 50 y 150
        cur.execute("""
            INSERT INTO practica.quota_anual (num_soci, data_pagament, import)
            VALUES (%s, %s, %s)
            ON CONFLICT (num_soci, data_pagament) DO NOTHING
        """, (membre, data_pagament, importe))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cur.close()
conn.close()

print("90,000 miembros insertados correctamente")
