from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birthdate = models.DateField()
    center = models.CharField(max_length=100)
    cycle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_photos', default='default.jpg')

    # Definir accesos inversos personalizados para evitar conflictos
    groups = models.ManyToManyField('auth.Group', related_name="biblioteca_user_groups", blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name="biblioteca_user_permissions", blank=True)
    
class TipusElement(models.Model):
    nom = models.CharField(max_length=100)

class ElementCatalog(models.Model):
    tipus_element = models.ForeignKey(TipusElement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    imatge = models.ImageField(upload_to='catalog_images', default='default_item.jpg')

class Exemplar(models.Model):
    element_catalog = models.ForeignKey(ElementCatalog, on_delete=models.CASCADE)

class Reserva(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    data_reserva = models.DateField()

class Prestec(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    data_prestec = models.DateField()
    data_retorn = models.DateField(null=True, blank=True)

class Peticio(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    data_peticio = models.DateField()
    complerta = models.BooleanField(default=False)

class Registre(models.Model):
    missatge = models.TextField()
    data_registre = models.DateTimeField(auto_now_add=True)
