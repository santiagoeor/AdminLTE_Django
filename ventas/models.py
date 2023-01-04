from django.db import models

# Create your models here.

class Producto(models.Model):
    referencia = models.IntegerField(max_length=50)
    producto = models.CharField(max_length=60)
    descricorta = models.CharField(max_length=50)
    descripcion = models.TextField()
    stock = models.IntegerField(max_length=20)
    valorcom = models.IntegerField(max_length=60)