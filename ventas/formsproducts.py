from django import forms
from django.core import validators

class FormProducto(forms.Form):
    txt_refer = forms.CharField(
        label = "Referencia",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control',
                # 'value': '{{ producto.id }}'
            }
        ),
        validators=[
            # validators.validate_integer(int, "Por favor un numero")
            # validators.integer_validator(2)
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )
    
    txt_Nombre = forms.CharField(
        label = "Nombre del Producto",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    txt_Descor = forms.CharField(
        label = "Descripción corta",
        widget=forms.Textarea,
        validators = [
            validators.MaxLengthValidator(30, 'Te has pasado, has puesto mucho texto')
        ]
    )
    txt_Descor.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'form-control'
    })

    txt_Descri = forms.CharField(
        label = "Coloque una Descripción",
        widget=forms.Textarea,
        validators = [
            validators.MaxLengthValidator(80, 'Te has pasado, has puesto mucho texto')
        ]
    )
    txt_Descri.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'form-control'
    })

    txt_cantEx = forms.CharField(
        label = "Cantidad Existente",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Stock',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )

    txt_vlrCom = forms.CharField(
        label = "Valor Comercial",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )

class FormProductoedit(forms.Form):
    txt_refer = forms.CharField(
        label = "Referencia",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control',
                # 'value': '{{ producto.id }}'
            }
        ),
        validators=[
            # validators.validate_integer(int, "Por favor un numero")
            # validators.integer_validator(2)
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )
    
    txt_Nombre = forms.CharField(
        label = "Nombre del Producto",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    txt_Descor = forms.CharField(
        label = "Descripción corta",
        widget=forms.Textarea,
        validators = [
            validators.MaxLengthValidator(30, 'Te has pasado, has puesto mucho texto')
        ]
    )
    txt_Descor.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'form-control'
    })

    txt_Descri = forms.CharField(
        label = "Coloque una Descripción",
        widget=forms.Textarea,
        validators = [
            validators.MaxLengthValidator(80, 'Te has pasado, has puesto mucho texto')
        ]
    )
    txt_Descri.widget.attrs.update({
        'placeholder': 'Mete el contenido YAA',
        'class': 'form-control'
    })

    txt_cantEx = forms.CharField(
        label = "Cantidad Existente",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Stock',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )

    txt_vlrCom = forms.CharField(
        label = "Valor Comercial",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Introduce la referencia',
                'class': 'form-control'
            }
        ),
        validators=[
            validators.RegexValidator('^[0-9]*$', 'Por favor introucir numero', 'invalid_title')
        ]
    )