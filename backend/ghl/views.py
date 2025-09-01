from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json

from .services.oauth_client import get_authorize_url, exchange_code_for_token
from .services.ghl_client import set_access_token, crear_contacto

def iniciar_oauth(request):
    """Redirige al login de GHL"""
    url = get_authorize_url()
    return HttpResponseRedirect(url)

def callback_oauth(request):
    """Recibe el code de GHL y pide el access_token"""
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"error": "Falta code en la URL"}, status=400)
    try:
        token_data = exchange_code_for_token(code)
        access_token = token_data.get("access_token")
        set_access_token(access_token)
        return JsonResponse({"message": "Autenticado con éxito", "token": access_token})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def enviar_contacto(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            result = crear_contacto(data)
            return JsonResponse(result, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)