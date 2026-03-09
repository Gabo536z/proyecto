from fastapi import FastAPI
import mysql.connector
import os
import joblib
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

modelo = joblib.load("model.pkl")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

class Persona(BaseModel):
    nombre: str
    edad: int


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


@app.get("/")
def root():
    return {"mensaje": "API funcionando"}


@app.post("/personas")
def crear_persona(persona: Persona):

    db = get_db()
    cursor = db.cursor()

    query = "INSERT INTO personas (nombre, edad) VALUES (%s, %s)"
    cursor.execute(query, (persona.nombre, persona.edad))
    db.commit()

    cursor.close()
    db.close()

    return {"mensaje": "Persona guardada"}


@app.get("/personas")
def listar_personas():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM personas")
    personas = cursor.fetchall()

    cursor.close()
    db.close()

    return personas


@app.post("/predict")
def predict(persona: Persona):

    pred = modelo.predict([[persona.edad]])

    return {
        "nombre": persona.nombre,
        "edad": persona.edad,
        "categoria": pred[0]
    }


    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Buscar la persona por id
    query = "SELECT * FROM personas WHERE id = %s"
    cursor.execute(query, (id,))
    persona = cursor.fetchone()

    cursor.close()
    db.close()

    if not persona:
        return {"error": "Persona no encontrada"}

    # Hacer la predicción con la edad
    pred = modelo.predict([[persona["edad"]]])

    return {
        "id": persona["id"],
        "nombre": persona["nombre"],
        "edad": persona["edad"],
        "categoria": pred[0]
    }