# File: app/web/main.py
from fastapi import FastAPI
import psycopg2
import os

app = FastAPI(title="AKS POC API", version="1.0.0")

def get_db():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

@app.get("/")
def root():
    return {"message": "AKS POC Web Server", "status": "running"}

@app.get("/health")
def health():
    try:
        conn = get_db()
        conn.close()
        return {"status": "healthy", "db": "connected"}
    except Exception as e:
        return {"status": "degraded", "db": str(e)}

@app.get("/items")
def get_items():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM items LIMIT 10;")
    rows = cur.fetchall()
    conn.close()
    return {"items": [{"id": r[0], "name": r[1]} for r in rows]}
