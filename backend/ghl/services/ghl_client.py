import os, requests

BASE_URL = os.getenv("GHL_BASE_URL", "https://services.leadconnectorhq.com")

# ⚠️ Guardamos el token en memoria para simplificar (luego puedes persistir en BD)
ACCESS_TOKEN = None

def set_access_token(token: str):
    global ACCESS_TOKEN
    ACCESS_TOKEN = token

def _headers():
    if not ACCESS_TOKEN:
        raise RuntimeError("No hay ACCESS_TOKEN, primero haz login con OAuth")
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

def crear_contacto(data: dict):
    url = f"{BASE_URL}/contacts/"
    resp = requests.post(url, json=data, headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()

def buscar_contactos(query: str):
    url = f"{BASE_URL}/contacts/search"
    resp = requests.get(url, params={"query": query}, headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()