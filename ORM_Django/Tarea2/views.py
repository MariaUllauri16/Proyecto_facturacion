from django.shortcuts import render, redirect
from django.http import HttpResponse
from Tarea2.models import Producto, DetalleFactura, Factura, Cliente
from Tarea2.forms import DetalleFacturaForm, FacturaForm, ClienteForm, ProductoForm


# Create your views here.

def index(request):
    cliente = Cliente.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Cliente', 'Acerca': 'Acerca del Blog', 'clientes': cliente}
    return render(request, 'index.html', opciones)


def cliente(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Cliente', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ClienteForm()
        opciones['form'] = form

    return render(request, 'cliente.html', opciones)


def editarcliente(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Cliente', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'cliente.html', opciones)


def eliminarcliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/')
    return render(request, 'eliminarcliente.html', {'Cliente': cliente})




def listarproducto(request):
    producto = Producto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Producto', 'Acerca': 'Acerca del Blog', 'productos': producto}
    return render(request, 'listarproducto.html', opciones)



def producto(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Producto', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto/')
    else:
        form = ProductoForm()
        opciones['form'] = form

    return render(request, 'producto.html', opciones)


def editarproducto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Producto', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/listarproducto/')

    return render(request, 'producto.html', opciones)


def eliminarproducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('/listarproducto/')
    return render(request, 'eliminarproducto.html', {'Producto': producto})



def listarfactura(request):
    factura = Factura.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Lista de Factura', 'Acerca': 'Acerca del Blog', 'facturas': factura}
    return render(request, 'listarfactura.html', opciones)


def eliminarfactura(request, id):
    factura = Factura.objects.get(id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('/listarventa/')
    return render(request, 'eliminarfactura.html', {'Factura': factura})
