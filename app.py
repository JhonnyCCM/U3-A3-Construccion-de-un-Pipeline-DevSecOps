import requests

def fetch_data(url):
    """
    Función para consumir servicios web externos.
    Nota: Contiene credenciales hardcodeadas (Vulnerabilidad SAST B105).
    """
    api_key = "12345-SUPER-SECRET-KEY"
    password = "SuperSecretPassword123!"
    response = requests.get(f"{url}?key={api_key}")
    return response.json()

def validate_connection():
    # Nueva funcionalidad menor simulada por el desarrollador
    return {"status": "ready"}

if __name__ == "__main__":
    print("Módulo de consumo de API iniciado...")
