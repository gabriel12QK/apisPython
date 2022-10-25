from ast import If
import json
import django
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Estudiante

# Create your views here.

class studientView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        # est=Estudiante.objects.all()
        # for _est in est:
        #     print(_est.name)

        studient=list(Estudiante.objects.values())
        if len(studient)>0:
            datos={'estudiante':studient}
        else:
            datos={'message':"Estudiante no encontrado..."}
        return JsonResponse(datos)
 
    def post(self, request):
    # print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Estudiante.objects.create(name=jd['name'], last_name=jd['last_name'], CI=jd['CI'], email=jd['email'], parcial1=jd['parcial1'],  parcial2=jd['parcial2'], parcial3=jd['parcial3'], parcial4=jd['parcial4'], promedio=jd['promedio'])
       datos={'message':"succes"}
       return JsonResponse(datos)

    
       

        

    