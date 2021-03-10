from django.db import models

# Create your models here.    
class Sponsor(models.Model):
    sponsor_id = models.IntegerField(primary_key = True, verbose_name = "Identificación")
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    description = models.TextField(verbose_name="Descripción")
    cost = models.IntegerField(verbose_name = "Costo")
    
    class Meta:
        verbose_name = "Apadrinamiento"
        verbose_name_plural = "Apadrinamientos"
        
    def __str__(self):
        return self.name

class Animal(models.Model):
    rut = models.IntegerField(primary_key = True, verbose_name = "RUT")
    name = models.CharField(max_length = 50, verbose_name = "Nombre")
    school = models.IntegerField(verbose_name = "Colegio")
    course = models.IntegerField(verbose_name = "Curso")
    instrucciones = models.TextField(verbose_name = "Instrucciones")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "Animales")
    document = models.FileField(verbose_name = "Documento", upload_to = "Documentos")
    #gender = models.CharField(max_length = 50, verbose_name = "Sexo", blank=True)
    #sterilized = models.CharField(max_length = 50, verbose_name = "Esterilizado", blank=True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de modificación")
    sponsors = models.ManyToManyField(Sponsor, through = "Animal_sponsor" , verbose_name = "Apadrinamientos")
 

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Animal_sponsor(models.Model):
    animal = models.ForeignKey(Animal, on_delete = models.CASCADE, verbose_name = "Animal")
    sponsor = models.ForeignKey(Sponsor, on_delete = models.CASCADE, verbose_name = "Apadrinamiento")
    
    class Meta:
        verbose_name = "Apadrinamiento de animal"
        verbose_name_plural = "Apadrinamientos de animales"

    #def __str__(self):
        #return "Apadrinamiento de ", self.animal