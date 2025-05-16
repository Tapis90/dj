from django.urls import path
from core import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('reporte_de_compras/', views.reporte_de_compras, name="reporte_de_compras"),
    path('reporte_de_ventas/', views.reporte_de_ventas, name="reporte_de_ventas"),
    path('agregar_proveedores/', views.agregar_proveedores, name="agregar_proveedores"),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('agregar_clientes/', views.agregar_clientes, name="agregar_clientes"),
    path('Producto/', views.producto, name="producto"),
    path('Venta/', views.venta, name="venta"),
    path('Usuario/', views.usuario, name="usuario"),
    path('Compra/', views.compra, name="compra"),
    path('Cliente/', views.cliente, name="cliente"),
]

