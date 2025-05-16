from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

def home(request):
    return render(request, 'index.html')

def reporte_de_compras(request):
    compra = Compra.objects.all
    data = {"compra":compra,}
    if request.method == "POST":
        cantidad = request.POST["cantidadCompra"]
        precio_unitario = request.POST["precioCompra"]
        Compra.objects.create(Cantidad = cantidad, Precio_unitario = precio_unitario, Fecha = datetime.now() )
    return render(request, 'reportedecompras.html',data)

def reporte_de_ventas(request):
    venta = Venta.objects.all
    data = {"venta":venta,}
    if request.method == "POST":
        cantidad = request.POST["cantidadVenta"]
        precio_unitario = request.POST["precioVenta"]
        Venta.objects.create(Cantidad = cantidad, Precio_unitario = precio_unitario, Fecha = datetime.now() )
    return render(request, 'reportedeventas.html',data)

def agregar_proveedores(request):
    usuario = Usuario.objects.all
    data = {"usuario":usuario,}
    if request.method == "POST":
        nombre = request.POST["nombreProveedor"]
        telefono = request.POST["telefonoProveedor"]
        Usuario.objects.create(Nombre = nombre, Telefono = telefono)
    return render(request, 'agregarproveedores.html',data)

def agregar_producto(request): 
    producto = Producto.objects.all
    data = {"producto":producto,}
    if request.method == "POST":
        nombre = request.POST["nombreProducto"]
        precio = request.POST["precioProducto"]
        cantidad = request.POST["cantidadProducto"]
        Producto.objects.create(Nombre = nombre, Precio = precio, Cantidad = cantidad, Fecha = datetime.now() )
    return render(request, 'agregarproducto.html',data)

def agregar_clientes(request):
    cliente = Cliente.objects.all
    data = {"cliente":cliente,}
    if request.method == "POST":
        nombre = request.POST["nombreCliente"]
        telefono = request.POST["telefonoCliente"]
        Cliente.objects.create(Nombre = nombre, Telefono = telefono)
    return render(request, 'agregarclientes.html',data)

def producto (request):
    Producto.objects.create(Nombre = "Nombre", Precio = "Precio", Cantidad = "Cantidad", Fecha = datetime.now() )
    return redirect('home')

def venta (request):
    Venta.objects.create(Cantidad = "Cantidad", Precio_unitario = "Precio_unitario", Fecha = datetime.now() )
    return redirect('home')

def compra (request):
    Compra.objects.create(Cantidad = "Cantidad", Precio_unitario = "Precio_unitario", Fecha = datetime.now() )
    return redirect('home')

def usuario(request):
    Usuario.objects.create(Nombre = "Nombre", Telefono = "Telefono", Cantidad = "Cantidad")
    return redirect('home')

def cliente(request):
    Cliente.objects.create(Nombre = "Nombre", Telefono = "Telefono", Cantidad = "Cantidad")
    return redirect('home')
# Create your views here.
