from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length= 100)
    email = models.CharField(max_length = 80)
    created_at = models.DateTimeField(auto_now_add=True)