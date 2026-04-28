from fastapi.testclient import TestClient
import random as r
from main import app

# Probar la api sum
def test_api_random_values():
    # Cliente
    client = TestClient(app)
    
    # Iterar valores aleatorios
    for _ in range(100):
        a = r.randint(-30, 30)
        b = r.randint(-30, 30)

        # Respuesta
        response = client.get(f"/sum?a={a}&b={b}")
        
        # Comprobar respuestas
        assert response.status_code == 200
        assert response.json() == (a+b)