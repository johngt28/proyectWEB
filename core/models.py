from django.db import models

# modelo consultas.

class contacto(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = 'Name')
    telefono = models.CharField(max_length = 100, verbose_name = 'Phone')
    email = models.CharField(max_length = 100, primary_key=True, verbose_name = 'Email')
    direccion = models.CharField(max_length = 100, verbose_name = 'Address')
    mensaje = models.CharField(max_length = 500, verbose_name = 'Message')