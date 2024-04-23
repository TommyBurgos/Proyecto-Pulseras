from django import forms
from django.forms import ModelForm
from user.models import User
from django.contrib.auth.hashers import check_password


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