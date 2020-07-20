from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from sinesp_client import SinespClient
# Create your views here.
def consultarPlaca(request, placa):
    try:
        sc = SinespClient()
        result = sc.search(placa)
        return JsonResponse(result)
    except:
        return HttpResponse('Placa inválida ou problema de conexão com a API ')