from django import forms
from django.forms import modelformset_factory
from user.models import User
from django.contrib.auth.hashers import check_password
from .models import BlogNoticia, Paquete, PaqueteImagen, Servicio


class registrarUsuario():
    print("")


class UserForm(forms.ModelForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
    new_password = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")
        print(old_password)
        print(new_password)
        print(confirm_new_password)

        if new_password != confirm_new_password:
            print("ENTRE AQUI PERO NO SE PARECEN LAS CONTRAS")
            raise forms.ValidationError("Las contraseñas nuevas no coinciden.")

        if self.instance.check_password(old_password):
            print("ENTRE AQUI PERO la contrasena actual no coincide")
            raise forms.ValidationError("La contraseña actual no es válida.")
        return cleaned_data


class BlogNoticiaForm(forms.ModelForm):
    class Meta:
        model = BlogNoticia
        fields = ['img', 'titulo', 'noticia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'noticia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here', 'rows': 5}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }


class PaqueteForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(
        queryset=Servicio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True  # Servicios son obligatorios
    )

    class Meta:
        model = Paquete
        fields = ['name', 'descripcion', 'descripcion_detallada', 'valor', 'servicios']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del paquete'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una breve descripción de su paquete ', 'rows': 2}),
            'descripcion_detallada': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escriba una descripción detallada de su paquete ', 'rows': 7}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PaqueteImagenForm(forms.ModelForm):
    class Meta:
        model = PaqueteImagen
        fields = ['imagen']
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

PaqueteImagenFormSet = modelformset_factory(PaqueteImagen, form=PaqueteImagenForm, extra=3)
