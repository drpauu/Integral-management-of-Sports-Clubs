import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

# Crear una instancia de Faker
fake = Faker()

# Conexión a la base de datos PostgreSQL
#conn = psycopg2.connect(
#    dbname="est_e7594959",
#    user="est_e7594959",
#    password="dB.e7594959",
#    host="localhost"
#)

conn = psycopg2.connect(
    dbname="est_c4414773",
    user="est_c4414773",
    password="dB.c4414773",
    host="localhost"
)
cur = conn.cursor()

# Generar datos ficticios
num_membres = 10000
num_equips = 1000
num_competicions = 500
num_entrenaments = 5000
num_patrocinadors = 100
num_paquets = 1000

# Crear un set para rastrear los num_soci únicos
num_soci_set = set()

# Insertar categories y guardar sus IDs
categories = ["PreBenjamí", "Benjamí", "Aleví", "Infantil", "Juvenil", "Junior", "Senior"]
categoria_ids = []
for categoria in categories:
    cur.execute("""
        INSERT INTO practica.categoria (nivell)
        VALUES (%s)
        ON CONFLICT (nivell) DO NOTHING
        RETURNING id
    """, (categoria,))
    result = cur.fetchone()
    if result:
        categoria_ids.append(result[0])
    else:
        cur.execute("SELECT id FROM practica.categoria WHERE nivell = %s", (categoria,))
        categoria_ids.append(cur.fetchone()[0])

# Insertar esports
esports = ["Futbol", "Bàsquet", "Handbol"]
for esport in esports:
    cur.execute("""
        INSERT INTO practica.esport (nom)
        VALUES (%s)
        ON CONFLICT (nom) DO NOTHING
    """, (esport,))

# Insertar membres
for _ in range(num_membres):
    while True:
        num_soci = random.randint(10000, 99999)
        if num_soci not in num_soci_set:
            num_soci_set.add(num_soci)
            break
    
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
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
    
    try:
        cur.execute("""
            INSERT INTO practica.membre (num_soci, nom, data_naixement, sexe, email)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (email) DO NOTHING
        """, (num_soci, nom, data_naixement, sexe, email))
    except psycopg2.errors.UniqueViolation:
        conn.rollback()

# Insertar cuotas anuales
cur.execute("SELECT num_soci FROM practica.membre")
membres = [row[0] for row in cur.fetchall()]

for membre in membres:
    for _ in range(random.randint(1, 3)):  # Cada miembro puede tener entre 1 y 3 cuotas anuales
        data_pagament = fake.date_between(start_date='-3y', end_date='today')
        importe = round(random.uniform(50, 150), 2)  # Importe entre 50 y 150
        cur.execute("""
            INSERT INTO practica.Quota_Anual (num_soci, data_pagament, import)
            VALUES (%s, %s, %s)
            ON CONFLICT (num_soci, data_pagament) DO NOTHING
        """, (membre, data_pagament, importe))

# Insertar equips
for _ in range(num_equips):
    nom = fake.word()
    categoria = random.choice(categoria_ids)
    esport = random.choice(esports)
    cur.execute("""
        INSERT INTO practica.equip (nom, categoria, esport)
        VALUES (%s, %s, %s)
        ON CONFLICT (nom) DO NOTHING
    """, (nom, categoria, esport))

# Insertar competicions
for _ in range(num_competicions):
    nom = fake.word()
    esport = random.choice(esports)
    categoria = random.choice(categoria_ids)
    any_celebracio = random.randint(2020, 2024)
    cur.execute("""
        INSERT INTO practica.competició (nom, esport, categoria, any_celebracio)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (nom) DO NOTHING
    """, (nom, esport, categoria, any_celebracio))

# Insertar membres_equips
cur.execute("SELECT num_soci FROM practica.membre")
membres = [row[0] for row in cur.fetchall()]

cur.execute("SELECT nom FROM practica.equip")
equips = [row[0] for row in cur.fetchall()]

for membre in membres:
    equip = random.choice(equips)
    data_inclusio = fake.date_between(start_date='-2y', end_date='today')
    cur.execute("""
        INSERT INTO practica.membre_equip (num_soci, nom_equip, data_inclusio)
        VALUES (%s, %s, %s)
        ON CONFLICT (num_soci, nom_equip) DO NOTHING
    """, (membre, equip, data_inclusio))

# Insertar participació_equip
cur.execute("SELECT nom FROM practica.competició")
competicions = [row[0] for row in cur.fetchall()]

for equip in equips:
    competicio = random.choice(competicions)
    data_participacio = fake.date_between(start_date='-2y', end_date='today')
    cur.execute("""
        INSERT INTO practica.participació_equip (nom_equip, nom_competicio, data_participacio)
        VALUES (%s, %s, %s)
        ON CONFLICT (nom_equip, nom_competicio) DO NOTHING
    """, (equip, competicio, data_participacio))

# Insertar estadístiques
for membre in membres:
    competicio = random.choice(competicions)
    partits_jugats = random.randint(1, 20)
    minuts_jugats = random.randint(30, 1800)
    cur.execute("""
        INSERT INTO practica.estadística (num_soci, nom_competicio, partits_jugats, minuts_jugats)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (num_soci, nom_competicio) DO NOTHING
        RETURNING id
    """, (membre, competicio, partits_jugats, minuts_jugats))
    result = cur.fetchone()
    if result:
        estadistica_id = result[0]

        esport = random.choice(esports)
        if esport == "Bàsquet":
            punts = random.randint(0, 50)
            assistencies = random.randint(0, 20)
            rebots = random.randint(0, 20)
            cur.execute("""
                INSERT INTO practica.estadística_bàsquet (id, punts, assistencies, rebots)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (estadistica_id, punts, assistencies, rebots))
        elif esport == "Futbol":
            gols = random.randint(0, 10)
            assistencies = random.randint(0, 10)
            targetes_grogues = random.randint(0, 5)
            cur.execute("""
                INSERT INTO practica.estadística_futbol (id, gols, assistencies, targetes_grogues)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (estadistica_id, gols, assistencies, targetes_grogues))
        elif esport == "Handbol":
            gols = random.randint(0, 10)
            assistencies = random.randint(0, 10)
            parades = random.randint(0, 10)
            cur.execute("""
                INSERT INTO practica.estadística_handbol (id, gols, assistencies, parades)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING
            """, (estadistica_id, gols, assistencies, parades))

# Insertar entrenaments
for _ in range(num_entrenaments):
    while True:
        data = fake.date_between(start_date='-1y', end_date='today')
        hora = fake.time()
        lloc = fake.city()
        esport = random.choice(esports)
        categoria = random.choice(categoria_ids)
        
        # Comprobar si la combinación (data, hora, esport, categoria) ya existe
        cur.execute("""
            SELECT COUNT(*) FROM practica.entrenament
            WHERE data = %s AND hora = %s AND esport = %s AND categoria = %s
        """, (data, hora, esport, categoria))
        if cur.fetchone()[0] == 0:
            break

    cur.execute("""
        INSERT INTO practica.entrenament (data, hora, lloc, esport, categoria)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (data, hora, esport, categoria) DO NOTHING
    """, (data, hora, lloc, esport, categoria))

# Insertar assistencia
for membre in membres:
    cur.execute("SELECT data, hora, esport, categoria FROM practica.entrenament ORDER BY RANDOM() LIMIT 1")
    entrenament = cur.fetchone()
    if entrenament:
        data, hora, esport, categoria = entrenament
        hora_str = hora.strftime('%H:%M:%S')  # Convertir time a string
        hora_arribada = (datetime.combine(data, datetime.strptime(hora_str, '%H:%M:%S').time()) + timedelta(minutes=random.randint(-15, 15))).time()
        duracio_entrenament = random.randint(30, 120)
        comentaris = fake.sentence()
        cur.execute("""
            INSERT INTO practica.assistencia (num_soci, data, hora, esport, categoria, hora_arribada, duracio_entrenament, comentaris)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (num_soci, data, hora) DO NOTHING
        """, (membre, data, hora, esport, categoria, hora_arribada, duracio_entrenament, comentaris))

# Insertar patrocinadors
for _ in range(num_patrocinadors):
    nom = fake.company()
    descripcio_beneficis = fake.sentence()
    cur.execute("""
        INSERT INTO practica.patrocinador (nom, descripcio_beneficis)
        VALUES (%s, %s)
        ON CONFLICT (nom) DO NOTHING
    """, (nom, descripcio_beneficis))

# Insertar paquets de patrocini
for _ in range(num_paquets):
    beneficis = fake.sentence()
    cur.execute("""
        INSERT INTO practica.paquet_de_patrocini (beneficis)
        VALUES (%s)
        RETURNING id
    """, (beneficis,))
    paquet_id = cur.fetchone()[0]

    # Asociar patrocinadors a paquets
    cur.execute("SELECT nom FROM practica.patrocinador ORDER BY RANDOM() LIMIT 2")
    patrocinadors = cur.fetchall()
    for patrocinador in patrocinadors:
        nom_patrocinador = patrocinador[0]
        data_acord = fake.date_between(start_date='-1y', end_date='today')
        duracio = random.randint(1, 12)
        condicions = fake.sentence()
        cur.execute("""
            INSERT INTO practica.acord_patrocinadors (nom_patrocinador, id_paquet, data_acord, duracio, condicions)
            VALUES (%s, %s, %s, %s, %s)
        """, (nom_patrocinador, paquet_id, data_acord, duracio, condicions))

    # Asociar paquets a equips
    equip = random.choice(equips)
    cur.execute("""
        INSERT INTO practica.patrocini_equip (nom_equip, id_paquet)
        VALUES (%s, %s)
        """, (equip, paquet_id))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cur.close()
conn.close()
