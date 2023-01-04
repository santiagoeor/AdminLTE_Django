from django.shortcuts import render, HttpResponse, redirect
from ventas.models import Producto
from django.contrib import messages

# Create your views here.

def login(request):
    return render(request, 'login.html')

def adminlte(request):
    return render(request, 'views_admin/admin.html')

def registproducts(request):
    
    return render(request, 'views_admin/regist_product.html')

def listproducts(request):

    productos = Producto.objects.order_by('id')

    return render(request, 'views_admin/list_products.html', {
        'productos': productos
    })

def guardar(request):
    if request.method == 'POST':

        refer = request.POST['txt_refer']
        nombre = request.POST['txt_Nombre']
        descripcorta = request.POST['txt_Descor']
        descripcion = request.POST['txt_Descri']
        Stock = request.POST['txt_cantEx']
        valor = request.POST['txt_vlrCom']

        if refer and Stock and valor == int:  
            producto = Producto(
                referencia = refer,
                producto = nombre,
                descricorta = descripcorta,
                descripcion = descripcion,
                stock = Stock,
                valorcom = valor,
            )

            producto.save()
            
            messages.success(request, 'Producto registrado')
            return redirect('productos')
        else:
            messages.success(request, 'Por favor digitar numeros')
            return redirect('productos')
    else:
        messages.success(request, 'No se a podido registrar')
        return redirect('productos')

def borrar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
     
    messages.success(request, 'Ha sido eliminado')
    return redirect('lisproduct')


    


