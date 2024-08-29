from django import forms
from .models import Shop
from django.forms import ModelForm


class CreationForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['product_name', 'price', 'image', 'item_type']


class LoginForm(forms.Form):
    username = forms.CharField(max_length='50')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['username', 'password']
