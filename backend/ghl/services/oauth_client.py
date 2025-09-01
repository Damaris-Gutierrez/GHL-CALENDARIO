import os, requests

CLIENT_ID = os.getenv("GHL_CLIENT_ID")
CLIENT_SECRET = os.getenv("GHL_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GHL_REDIRECT_URI")

# OJO: authorize va al marketplace
AUTH_URL = "https://marketplace.gohighlevel.com/oauth/authorize"
TOKEN_URL = "https://services.leadconnectorhq.com/oauth/token"

def get_authorize_url():
    return f"{AUTH_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"

def exchange_code_for_token(code: str):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    resp = requests.post(TOKEN_URL, data=data, timeout=30)
    resp.raise_for_status()
    return resp.json()