from django import forms
from .models import DetalleFactura, Producto, Factura, Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')
        labels = {'ruc': 'ruc', 'nombre': 'nombre', 'direccion': 'direccion', 'producto': 'producto'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        labels = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'Iva'}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'iva': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', 'total')
        label = {'cliente': 'Cliente', 'fecha': 'Fecha', 'total': 'Total'}
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ('factura', 'producto', 'cantidad', 'precio', 'subtotal')
        label = {'factura': 'Factura', 'producto': 'Producto', 'cantidad': 'Cantidad', 'precio': 'Precio',
                 'subtotal': 'Subtotal'}
        widgets = {
            'factura': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'subtotal': forms.TextInput(attrs={'class': 'form-control'}),
        }
