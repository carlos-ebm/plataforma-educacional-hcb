from django.db import models
from registration.models import Profile

# Create your models here.    
class Activity(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    instruction = models.TextField(verbose_name = "Instrucciones")
    document = models.FileField(verbose_name = "Documento", upload_to = "Documentos")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")
    activityToProfile = models.ManyToManyField(Profile, through = "Activity_profile" , verbose_name = "Actividades de perfiles")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Activity_profile(models.Model):
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")

    class Meta:
        verbose_name = "Actividad de perfil"
        verbose_name_plural = "Actividades de perfiles"
        ordering = ["-created"]

    def __str__(self):
        message = str(self.activity) +" asignada/o a "+ str(self.profile)
        return message
