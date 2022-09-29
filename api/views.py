from django.views import View
from .models import Empleado
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

# Create your views here.
class EmpleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
                empleados=list(Empleado.objects.filter(id=id).values())
                if len(empleados) > 0:
                    empleado=empleados[0]
                    data={'message':'Success', 'empleados':empleado}
                else:
                    data={'message':'Empleado no encontrado...'}
                return JsonResponse(data)

        else:
                empleados= list(Empleado.objects.values())
                if len(empleados)>0:
                        data={'message':'Success', 'empleados':empleados}
                else:
                        data={'message':'Empleados no encontrados...'}
                return JsonResponse(data)

    def post(self, request):
        jr=json.loads(request.body)
        Empleado.objects.create(nombre=jr['nombre'],apellido=jr['apellido'], email=jr['email'] )
        data = {'message': 'Success'}
        return JsonResponse(data)

    def put(self, request, id):
        jr=json.loads(request.body)
        empleados=list(Empleado.objects.filter(id=id).values())
        if len(empleados) > 0:
            empleado=Empleado.objects.get(id=id)
            empleado.nombre=jr['nombre']
            empleado.apellido=jr['apellido']
            empleado.email=jr['email']
            empleado.save()
            data={'message':'Success'}
        else:
            data={'message':'Empleado no encontrado...'}
        return JsonResponse(data)


    def delete(self, request, id):
        empleados=list(Empleado.objects.filter(id=id).values())
        if len(empleados) >0:
            Empleado.objects.filter(id=id).delete()
            data = {"message": "Empleado eliminado"}
        else:
            data = {"message": "Empleado no encontrado"}
        return JsonResponse(data)