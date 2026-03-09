import requests

BASE_URL = "http://localhost:8000"


def test_root():
    r = requests.get(BASE_URL + "/")
    assert r.status_code == 200


def test_crear_persona():

    data = {
        "nombre": "Test",
        "edad": 20
    }

    r = requests.post(BASE_URL + "/personas", json=data)
    assert r.status_code == 200


def test_listar_personas():

    r = requests.get(BASE_URL + "/personas")

    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_predict():

    data = {
        "nombre": "Test",
        "edad": 15
    }

    r = requests.post(BASE_URL + "/predict", json=data)
    assert r.status_code == 200