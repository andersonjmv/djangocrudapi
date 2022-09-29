from django.urls import path
from .views import EmpleadoView

urlpatterns = [
    path('empleados/', EmpleadoView.as_view(), name='empleados_list'),
    path('empleados/<int:id>', EmpleadoView.as_view(), name='empleados_detail')

]