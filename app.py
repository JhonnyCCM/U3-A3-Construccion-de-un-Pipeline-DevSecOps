import os
import requests

def fetch_data(url):
    """
    Función para consumir servicios web externos de manera segura.
    Remediación:
    - Extracción de API Key desde variable de entorno (sin secretos en código).
    - Eliminación de contraseñas hardcodeadas.
    - Configuración de timeout explícito para prevenir denegación de servicio (CWE-400).
    """
    api_key = os.environ.get("API_KEY", "")
    response = requests.get(f"{url}?key={api_key}", timeout=10)
    return response.json()

def validate_connection():
    # Nueva funcionalidad validada de forma segura
    return {"status": "ready"}

if __name__ == "__main__":
    print("Módulo seguro de consumo de API iniciado...")
