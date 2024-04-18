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

class ItemType(models.Model):
    name = models.CharField(max_length=100)

class CatalogItem(models.Model):
    # Eliminar la relación con Catalog
    # catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='catalog_images', default='default_item.jpg')

class Copy(models.Model):
    catalog_item = models.ForeignKey(CatalogItem, on_delete=models.CASCADE)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    reserved_date = models.DateField()

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateField()
    fulfilled = models.BooleanField(default=False)

class Log(models.Model):
    message = models.TextField()
    log_date = models.DateTimeField(auto_now_add=True)
