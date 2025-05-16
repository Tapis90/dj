from django.db import models


class Venta(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    Cantidad = models.CharField(max_length=100, blank=True, default='')
    Precio_unitario = models.CharField(max_length=100, blank=True, default='')
    Fecha = models.DateTimeField()


    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

from django.db import models

class Compra(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    Cantidad = models.IntegerField()
    Precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateTimeField()

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

class Producto(models.Model):
    # imagen_plano = models.ImageField(upload_to="plano_ubicacion", blank=True, default='')
    id = models.BigAutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100, blank=True, default='')
    Precio = models.CharField(max_length=100, blank=True, default='')
    Cantidad = models.CharField(max_length=100, blank=True, default='')
    Fecha = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

class Usuario(models.Model):
    # imagen_plano = models.ImageField(upload_to="plano_ubicacion", blank=True, default='')
    id = models.BigAutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100, blank=True, default='')
    Telefono = models.CharField(max_length=100, blank=True, default='')
    Cantidad = models.CharField(max_length=100, blank=True, default='')
    tipo_usuario = models.CharField(max_length=1, blank=True, default='')

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

class Cliente(models.Model):
    # imagen_plano = models.ImageField(upload_to="plano_ubicacion", blank=True, default='')
    id = models.BigAutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=100, blank=True, default='')
    Telefono = models.CharField(max_length=100, blank=True, default='')
    Cantidad = models.CharField(max_length=100, blank=True, default='')
    tipo_usuario = models.CharField(max_length=1, blank=True, default='')

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"