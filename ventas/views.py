from django.shortcuts import render, HttpResponse, redirect
from ventas.models import Producto
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_venta(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin')
        else:
            messages.warning(request, 'Has ingresado algo mal')


    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def adminlte(request):
    return render(request, 'views_admin/admin.html')

@login_required(login_url="login")
def registproducts(request):
    
    return render(request, 'views_admin/regist_product.html')

@login_required(login_url="login")
def listproducts(request):

    busqueda = request.GET.get('txtBuscar')
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter(
            Q(producto__icontains = busqueda) |
            Q(descricorta__icontains = busqueda)
        ).distinct()

    return render(request, 'views_admin/list_products.html', {
        'productos': productos
    })

@login_required(login_url="login")
def guardar(request):
    if request.method == 'POST':

        refer = request.POST['txt_refer']
        nombre = request.POST['txt_Nombre']
        descripcorta = request.POST['txt_Descor']
        descripcion = request.POST['txt_Descri']
        Stock = request.POST['txt_cantEx']
        valor = request.POST['txt_vlrCom']

        # if refer and Stock and valor == int:  
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
        # else:
        #     messages.success(request, 'Por favor digitar numeros')
            # return redirect('productos')
    else:
        messages.success(request, 'No se a podido registrar')
        return redirect('productos')

@login_required(login_url="login")
def borrar_producto(request, id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
     
    messages.success(request, 'Ha sido eliminado')
    return redirect('lisproduct')

@login_required(login_url="login")
def editar_producto(request, id):

    producto = Producto.objects.get(pk=id)

    return render(request, 'views_admin/edit_product.html', {
        'producto': producto
    })

@login_required(login_url="login")
def editar(request):

    if request.method == 'POST':
       id = request.POST['txt_id']

       producto = Producto.objects.get(pk=id)
       producto.referencia = request.POST['txt_refer']
       producto.producto = request.POST['txt_Nombre']
       producto.descricorta = request.POST['txt_Descor']
       producto.descripcion = request.POST['txt_Descri']
       producto.stock = request.POST['txt_cantEx']
       producto.valorcom = request.POST['txt_vlrCom']

       producto.save()

       return redirect('lisproduct')
    


