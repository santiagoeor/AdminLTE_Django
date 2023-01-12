from django.shortcuts import render, HttpResponse, redirect
from ventas.models import Producto
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ventas.formsproducts import FormProducto

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
        formproduct = FormProducto(request.POST)
        if formproduct.is_valid():
            data_form = formproduct.cleaned_data
            #datos del formulario
            refer = data_form.get('txt_refer')
            nombre = data_form.get('txt_Nombre')
            descripcorta = data_form.get('txt_Descor')
            descripcion = data_form.get('txt_Descri')
            Stock = data_form.get('txt_cantEx')
            valor = data_form.get('txt_vlrCom')
            #envindolos a la base de datos
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
            return redirect('save')

    else:
        formproduct = FormProducto()
        

    return render(request, 'views_admin/regist_product.html', {
    'formu': formproduct
    })

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


# def editar(request):

#     if request.method == 'POST':
#         Formproductoedit = FormProductoedit(request.POST)
#         if Formproductoedit.is_valid():
#             # data_form = Formproductoedit.cleaned_data
#             # id = request.POST['txt_id']
#             # # id = data_form.get('txt_id')
#             # producto = Producto.objects.get(pk=id)
#             # producto.referencia = data_form.get('txt_refer')
#             # producto.producto = data_form.get('txt_Nombre')
#             # producto.descricorta =data_form.get('txt_Descor') 
#             # producto.descripcion =data_form.get('txt_Descri') 
#             # producto.stock = data_form.get('txt_cantEx')
#             # producto.valorcom =data_form.get('txt_vlrCom')

#             # producto.save()
#             return redirect('lisproduct')

#     else:
#         return redirect('save')

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

       messages.success(request, f'{producto.producto} actualizado')
       return redirect('lisproduct')
    
