from django.db import models

# Create your models here.    
class Activity(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    school = models.IntegerField(verbose_name = "Colegio")
    course = models.IntegerField(verbose_name = "Curso")
    instruction = models.TextField(verbose_name = "Instrucciones")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "Animales")
    document = models.FileField(verbose_name = "Documento", upload_to = "Documentos")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.name
