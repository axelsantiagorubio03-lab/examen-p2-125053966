from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2, os

app = FastAPI(title="DataMart API")

def get_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "datamart"),
        user=os.getenv("POSTGRES_USER", "hadoop_user"),
        password=os.getenv("POSTGRES_PASSWORD", "hadoop_pass")
    )

class ResultadoSchema(BaseModel):
    clave: str
    subclave: str
    valor: float

@app.get("/resultados")
def get_all():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, clave, subclave, valor FROM resultados;")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return [{"id": r[0], "clave": r[1], "subclave": r[2], "valor": float(r[3])} for r in rows]

@app.get("/resultados/{clave}")
def get_by_clave(clave: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, clave, subclave, valor FROM resultados WHERE clave = %s;", (clave,))
    rows = cur.fetchall()
    cur.close(); conn.close()
    if not rows:
        raise HTTPException(status_code=404, detail="Clave no encontrada")
    return [{"id": r[0], "clave": r[1], "subclave": r[2], "valor": float(r[3])} for r in rows]

@app.post("/resultados")
def create_resultado(item: ResultadoSchema):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO resultados (clave, subclave, valor) VALUES (%s, %s, %s) RETURNING id;",
                (item.clave, item.subclave, item.valor))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close(); conn.close()
    return {"id": new_id, **item.dict()}