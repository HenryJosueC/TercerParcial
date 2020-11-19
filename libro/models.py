from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Libro (models.Model):
    autor= models.CharField(max_length=80)
    titulo = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=200)
    Categoria = models.ForeignKey(
        Categoria, related_name='libro', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
