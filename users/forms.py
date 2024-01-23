from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ApplicantCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password']

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                return forms.ValidationError('Las contraseñas no son iguales')
            return cd['password2']