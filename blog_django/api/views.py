from unicodedata import name
from django.http.response import JsonResponse
from django.views import View
from .models import Miembro
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.




class miembroView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            miembros=list(Miembro.objects.filter(id=id).values())
            if len (miembros)>0:
                miembro= miembros[0]
                datos = {'message':"Encontrados!",'miembros':miembro}
                return JsonResponse(datos)

            else:
                datos = {'message':"miembros no encontrados"}
                return JsonResponse(datos)

        else:  
            miembros = list(Miembro.objects.values()) #se obtiene una lista de python
            if len(miembros)>0:
                datos = {'message':"Encontrados!",'miembros':miembros} #creo un diccionario que muestra un mensaje y los miembros
            else:
                datos = {'message':"miembros no encontrados"}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Miembro.objects.create(nombre = jd['nombre'],apellido = jd['apellido'],email = jd ['email'])
        datos = {'message':"Encontrados!"}
        return JsonResponse(datos)
    def putt(self, request):
        pass
    def delete(self,request):
        pass
