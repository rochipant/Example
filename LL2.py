import pandas as pd
import psycopg2

# Paso 1: Leer el archivo CSV transformado
df = pd.read_csv("data/processed/transformed_data.csv")

# Paso 2: Conectar a la base de datos
conn = psycopg2.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    dbname="your_database"
)
cur = conn.cursor()

# Paso 3: Insertar los datos en la base de datos
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO your_table (id, name, value, value_n)
        VALUES (%s, %s, %s, %s)
    """, (row["id"], row["name"], row["value"], row["value_n"]))

# Paso 4: Confirmar y cerrar la conexión
conn.commit()
cur.close()
conn.close()

print("Ok")

