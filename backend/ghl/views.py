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
        return JsonResponse({"status": response.status_code, "raw": response.text}, status=response.status_code)

@csrf_exempt
def ping(request):
    """Prueba simple de conexión a la API de GHL"""
    url = f"{settings.GHL_BASE_URL}/calendars/"
    try:
        response = requests.get(url, headers=get_headers())
        return safe_json_response(response)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def calendars(request):
    """Obtener lista de calendarios de la subcuenta asociada al token"""
    url = f"{settings.GHL_BASE_URL}/calendars/"
    
    # Query params opcionales
    params = {}
    if getattr(settings, "GHL_LOCATION_ID", None):
        params["locationId"] = settings.GHL_LOCATION_ID

    # showDrafted opcional
    show_drafted = request.GET.get("showDrafted")
    if show_drafted is not None:
        params["showDrafted"] = show_drafted.lower() == "true"

    try:
        response = requests.get(url, headers=get_headers(), params=params)
        return safe_json_response(response)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def calendar_detail(request, calendar_id):
    """Detalle de un calendario específico"""
    url = f"{settings.GHL_BASE_URL}/calendars/{calendar_id}"
    try:
        response = requests.get(url, headers=get_headers())
        return safe_json_response(response)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
