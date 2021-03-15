from django.db import models
from django.contrib.auth.models import User
from school.models import Activity


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
   
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__username']

    def __str__(self):
        return self.fname

    
