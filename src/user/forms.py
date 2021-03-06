from django import forms
from .models import Profile
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput(attrs={'class':'form-control'}),
        }
