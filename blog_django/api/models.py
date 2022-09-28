from django.db import models

# Create your models here.

class Miembro(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.URLField(max_length=200)