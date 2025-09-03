# ghl/views.py

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_headers():
    """
    Headers correctos según documentación GHL:
    - Authorization: Bearer <token>
    - Version: 2021-04-15
    - Accept: application/json
    """
    return {
        "Authorization": f"Bearer {settings.GHL_PRIVATE_TOKEN}",
        "Version": "2021-04-15",
        "Accept": "application/json"
    }


def safe_json_response(response):
    """
    Retorna JsonResponse seguro.
    Si falla, devuelve status y texto crudo.
    """
    try:
        return JsonResponse(response.json(), safe=False, status=response.status_code)
    except Exception:
        return JsonResponse(
            {"status": response.status_code, "raw": response.text},
            status=response.status_code
        )


@csrf_exempt
def ping(request):
    """
    Ejercicio 3:
    Prueba simple de conexión a la API de GHL.
    Hace un GET a /calendars/ con locationId.
    """
    url = f"{settings.GHL_BASE_URL}/calendars/"

    if not getattr(settings, "GHL_LOCATION_ID", None):
        return JsonResponse({"error": "Falta configurar GHL_LOCATION_ID en settings.py"}, status=400)

    params = {"locationId": settings.GHL_LOCATION_ID}

    try:
        response = requests.get(url, headers=get_headers(), params=params)
        return safe_json_response(response)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def calendars(request):
    """
    Ejercicio 4:
    Obtener lista de calendarios de la subcuenta asociada al token.
    """
    url = f"{settings.GHL_BASE_URL}/calendars/"

    if not getattr(settings, "GHL_LOCATION_ID", None):
        return JsonResponse({"error": "Falta configurar GHL_LOCATION_ID en settings.py"}, status=400)

    # Query params
    params = {"locationId": settings.GHL_LOCATION_ID}

    show_drafted = request.GET.get("showDrafted")
    if show_drafted is not None:
        params["showDrafted"] = show_drafted.lower() == "true"

    try:
        response = requests.get(url, headers=get_headers(), params=params)

        if response.status_code == 200:
            data = response.json()
            # Simplificamos para frontend: solo id, name, status
            simplified = [
                {
                    "id": cal.get("id"),
                    "name": cal.get("name"),
                    "status": "Activo" if cal.get("isActive") else "Inactivo"
                }
                for cal in data.get("calendars", [])
            ]
            return JsonResponse({"calendars": simplified}, safe=False)

        return safe_json_response(response)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def calendar_detail(request, calendar_id):
    """
    Detalle de un calendario específico (extra).
    """
    url = f"{settings.GHL_BASE_URL}/calendars/{calendar_id}"
    try:
        response = requests.get(url, headers=get_headers())
        return safe_json_response(response)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
