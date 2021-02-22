from django import forms
from django.forms import ModelForm

from .models import User

class User_form(ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password']
        widgets = {
            'user_id': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
        labels = {
            'user_id': '账号',
            'password': '密码',
        }