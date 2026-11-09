import os, sys
import psycopg2

db_host = os.getenv("POSTGRES_HOST", "db")
db_name = os.getenv("POSTGRES_DB", "datamart")
db_user = os.getenv("POSTGRES_USER", "hadoop_user")
db_pass = os.getenv("POSTGRES_PASSWORD", "hadoop_pass")

conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        id SERIAL PRIMARY KEY,
        clave VARCHAR(100),
        subclave VARCHAR(100),
        valor NUMERIC(15, 2)
    );
""")
conn.commit()

resultado_file = sys.argv[1] if len(sys.argv) > 1 else "/tmp/part-00000"

with open(resultado_file, "r") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) == 3:
            c, sc, v = parts
        elif len(parts) == 2:
            c, sc, v = parts[0], "N/A", parts[1]
        else:
            continue
        cur.execute("INSERT INTO resultados (clave, subclave, valor) VALUES (%s, %s, %s)", (c, sc, float(v)))

conn.commit()
cur.close()
conn.close()
print("Resultados cargados exitosamente en la BD.")