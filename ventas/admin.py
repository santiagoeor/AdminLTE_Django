from django.contrib import admin
from .models import Producto

# Register your models here.



admin.site.register(Producto)

#configurar el titulo del panel
title = "Inventario de productos"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestion"
