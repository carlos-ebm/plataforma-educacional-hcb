from django.db import models
from django.contrib.auth.models import User
from shelter.models import Activity


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name = "Imagen", upload_to = "Perfiles", null=True, blank=True)
    fname = models.CharField(max_length = 50, verbose_name = "Nombre")
    lname = models.CharField(max_length = 50, verbose_name = "Apellido")
    email = models.EmailField(verbose_name = "E-mail")
    phone = models.CharField(max_length = 50, verbose_name = "Celular", blank=True)
    course = models.IntegerField(verbose_name = "Curso", null=True, blank=True)
    school = models.IntegerField(verbose_name = "Colegio", null=True, blank=True)
    address = models.CharField(max_length = 50, verbose_name = "Direccion", null=True, blank=True)
    activityToStudent = models.ManyToManyField(Activity, through = "Profile_activity" , verbose_name = "Actividades por estudiante")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__username']

    def __str__(self):
        return self.fname

    

class Profile_activity(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")

    class Meta:
        verbose_name = "Actividad de estudiante"
        verbose_name_plural = "Actividades de estudiantes"
        ordering = ["-created"]
