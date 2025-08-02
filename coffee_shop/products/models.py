from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=250, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    photo = models.ImageField(
        upload_to="Logos", null=True, blank=True, verbose_name="foto"
    )

    def __str__(self):
        return self.name
